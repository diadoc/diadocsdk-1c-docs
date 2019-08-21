# -*- coding: utf-8 -*-

import re
from six import iteritems

from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, ObjType, Index
from sphinx.locale import _, __
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.nodes import make_refnode


logger = logging.getLogger(__name__)

py_sig_re = re.compile(
    r'''^ ([\w.]*\.)?            # class name(s)
          (\w+)  \s*             # thing name
          (?: \(\s*(.*)\s*\)     # optional: arguments
           (?:\s* -> \s* (.*))?  #           return annotation
          )? $                   # and nothing more
          ''', re.VERBOSE)


def _pseudo_parse_arglist(signode, arglist):
    paramlist = addnodes.desc_parameterlist()
    stack = [paramlist]
    try:
        for argument in arglist.split(','):
            argument = argument.strip()
            ends_open = ends_close = 0
            while argument.startswith('['):
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                argument = argument[1:].strip()
            while argument.startswith(']'):
                stack.pop()
                argument = argument[1:].strip()
            while argument.endswith(']') and not argument.endswith('[]'):
                ends_close += 1
                argument = argument[:-1].strip()
            while argument.endswith('['):
                ends_open += 1
                argument = argument[:-1].strip()
            if argument:
                stack[-1] += addnodes.desc_parameter(argument, argument)
            while ends_open:
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                ends_open -= 1
            while ends_close:
                stack.pop()
                ends_close -= 1
        if len(stack) != 1:
            raise IndexError
    except IndexError:
        signode += addnodes.desc_parameterlist()
        signode[-1] += addnodes.desc_parameter(arglist, arglist)
    else:
        signode += paramlist


class ComObjectBase(ObjectDescription):
    option_spec = dict()
    doc_field_types = []
    allow_nesting = False

    def get_signature_prefix(self, sig):
        return ''

    def needs_arglist(self):
        return False

    def handle_signature(self, sig, signode):
        m = py_sig_re.match(sig)
        if m is None:
            raise ValueError
        name_prefix, name, arglist, retann = m.groups()

        classname, fullname = (name_prefix.rstrip('.'), name_prefix + name) if name_prefix else ('', name)

        signode['class'] = classname
        signode['fullname'] = fullname

        if name_prefix:
            signode += addnodes.desc_addname(name_prefix, name_prefix)

        signode += addnodes.desc_name(name, name)
        if not arglist:
            if self.needs_arglist():
                signode += addnodes.desc_parameterlist()
            return fullname, name_prefix

        _pseudo_parse_arglist(signode, arglist)
        return fullname, name_prefix

    def get_index_text(self, modname, name):
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls, sig, signode):
        fullname = name_cls[0]
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['ComObject']['objects']
            objects[fullname] = (self.env.docname, self.objtype)

        indextext = self.get_index_text(None, name_cls)
        if indextext:
            self.indexnode['entries'].append(('single', indextext, fullname, '', None))

    def before_content(self):
        prefix = None
        if self.names:
            (fullname, name_prefix) = self.names[-1]
            if name_prefix:
                prefix = name_prefix.strip('.')
        if prefix:
            self.env.ref_context['comobject'] = prefix

    def after_content(self):
        self.env.ref_context['comobject'] = None


class ComObjectClassmember(ComObjectBase):
    def needs_arglist(self):
        return self.objtype.endswith('method')

    def get_signature_prefix(self, sig):
        return ''

    def get_index_text(self, modname, name_cls):
        name, cls = name_cls
        result = ''
        if self.objtype == 'method':
            clsname, methname = name.rsplit('.', 1)
            result = _('{}() ({} method)'.format(methname, clsname))

        return result


class ComObjectXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        refnode['comobject'] = env.ref_context.get('comobject')
        if not has_explicit_title:
            title = title.lstrip('.')

        if target[0] == '.':
            target = target[1:]
            refnode['refspecific'] = True
        return title, target


class ComObjectIndex(Index):
    name = 'comobjectindex'
    localname = _('ComObject Index')
    shortname = _('comobjects')

    def generate(self, docnames=None):
        return [], False


class ComObjectDomain(Domain):
    name = 'ComObject'
    label = 'ComObject'
    object_types = {
        'method': ObjType(_('method'), 'meth'),
    }

    directives = {
        'method': ComObjectClassmember
    }
    roles = {
        'meth': ComObjectXRefRole(fix_parens=True),
    }
    initial_data = {
        'objects': {}
    }
    indices = [
        ComObjectIndex,
    ]

    def clear_doc(self, docname):
        for fullname, (fn, _l) in list(self.data['objects'].items()):
            if fn == docname:
                del self.data['objects'][fullname]

    def find_obj(self, name, type, searchmode=0):
        if name[-2:] == '()':
            name = name[:-2]

        if not name:
            return []

        objects = self.data['objects']
        matches = []

        if searchmode == 1:
            objtypes = list(self.object_types) if type is None else self.objtypes_for_role(type)
            if objtypes is not None:
                searchname = '.' + name
                matches = [(oname, objects[oname]) for oname in objects
                           if oname.endswith(searchname) and objects[oname][1] in objtypes]
        else:
            if name in objects:
                matches.append((name, objects[name]))
        return matches

    def resolve_xref(self, env, fromdocname, builder, type, target, node, contnode):
        searchmode = node.hasattr('refspecific') and 1 or 0
        matches = self.find_obj(target, type, searchmode)
        if not matches:
            return None
        elif len(matches) > 1:
            match_list = ', '.join(match[0] for match in matches)
            warning = 'more than one target found for cross-reference {}: {}'.format(target.repr(), match_list)
            logger.warning(__(warning), type='ref', subtype='comobject', location=node)
        name, obj = matches[0]

        return make_refnode(builder, fromdocname, obj[0], name, contnode, name)

    def get_objects(self):
        for refname, (docname, type) in iteritems(self.data['objects']):
            yield (refname, refname, type, docname, refname, 1)

    def get_full_qualified_name(self, node):
        target = node.get('reftarget')
        return None if target is None else '.'.join(filter(None, [None, target]))


def setup(app):
    app.add_domain(ComObjectDomain)

    return {
        'version': 'builtin',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
