# -*- coding: utf-8 -*-

import re

from docutils import nodes
from docutils.parsers.rst import directives
from six import iteritems

from sphinx import addnodes, locale
from sphinx.deprecation import DeprecatedDict, RemovedInSphinx30Warning
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, ObjType, Index
from sphinx.locale import _, __
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.docfields import Field, GroupedField, TypedField
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_refnode


logger = logging.getLogger(__name__)

py_sig_re = re.compile(
    r'''^ ([\w.]*\.)?            # class name(s)
          (\w+)  \s*             # thing name
          (?: \(\s*(.*)\s*\)     # optional: arguments
           (?:\s* -> \s* (.*))?  #           return annotation
          )? $                   # and nothing more
          ''', re.VERBOSE)


pairindextypes = {
    'module':    _('module'),
    'keyword':   _('keyword'),
    'operator':  _('operator'),
    'object':    _('object'),
    'exception': _('exception'),
    'statement': _('statement'),
    'builtin':   _('built-in function'),
}

locale.pairindextypes = DeprecatedDict(
    pairindextypes,
    'sphinx.locale.pairindextypes is deprecated. '
    'Please use sphinx.domains.python.pairindextypes instead.',
    RemovedInSphinx30Warning
)


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


class ComObjectXrefMixin(object):
    def make_xref(self,
                  rolename,
                  domain,
                  target,
                  innernode=nodes.emphasis,
                  contnode=None,
                  env=None,
                  ):
        result = super(ComObjectXrefMixin, self).make_xref(rolename, domain, target,
                                                    innernode, contnode, env)
        result['refspecific'] = True
        if target.startswith(('.', '~')):
            prefix, result['reftarget'] = target[0], target[1:]
            if prefix == '.':
                text = target[1:]
            elif prefix == '~':
                text = target.split('.')[-1]
            for node in result.traverse(nodes.Text):
                node.parent[node.parent.index(node)] = nodes.Text(text)
                break
        return result

    def make_xrefs(self,
                   rolename,
                   domain,
                   target,
                   innernode=nodes.emphasis,
                   contnode=None,
                   env=None,
                   ):
        # type: (...) -> List[nodes.Node]
        delims = r'(\s*[\[\]\(\),](?:\s*or\s)?\s*|\s+or\s+)'
        delims_re = re.compile(delims)
        sub_targets = re.split(delims, target)

        split_contnode = bool(contnode and contnode.astext() == target)

        results = []
        for sub_target in filter(None, sub_targets):
            if split_contnode:
                contnode = nodes.Text(sub_target)

            if delims_re.match(sub_target):
                results.append(contnode or innernode(sub_target, sub_target))
            else:
                results.append(self.make_xref(rolename, domain, sub_target,
                                              innernode, contnode, env))

        return results


class ComObjectField(ComObjectXrefMixin, Field):
    def make_xref(self, rolename, domain, target,
                  innernode=nodes.emphasis, contnode=None, env=None):
        if rolename == 'class' and target == 'None':
            rolename = 'obj'

        return super(ComObjectField, self).make_xref(rolename, domain, target,
                                              innernode, contnode, env)


class ComObjectGroupedField(ComObjectXrefMixin, GroupedField):
    pass


class ComObjectTypedField(ComObjectXrefMixin, TypedField):
    def make_xref(self, rolename, domain, target,
                  innernode=nodes.emphasis, contnode=None, env=None):
        if rolename == 'class' and target == 'None':
            rolename = 'obj'

        return super(ComObjectTypedField, self).make_xref(rolename, domain, target,
                                                   innernode, contnode, env)


class ComObjectBase(ObjectDescription):
    option_spec = {
        'noindex': directives.flag,
        'module': directives.unchanged,
        'annotation': directives.unchanged,
    }

    doc_field_types = [
        ComObjectTypedField('parameter',
                            label=_('Parameters'),
                            names=('param', 'parameter', 'arg', 'argument', 'keyword', 'kwarg', 'kwparam'),
                            typerolename='class',
                            typenames=('paramtype', 'type'),
                            can_collapse=True),
        ComObjectTypedField('variable',
                            label=_('Variables'),
                            rolename='obj',
                            names=('var', 'ivar', 'cvar'),
                            typerolename='class',
                            typenames=('vartype',),
                            can_collapse=True),
        ComObjectGroupedField('exceptions',
                              label=_('Raises'),
                              rolename='exc',
                              names=('raises', 'raise', 'exception', 'except'),
                              can_collapse=True),
        Field('returnvalue',
              label=_('Returns'),
              has_arg=False,
              names=('returns', 'return')),
        ComObjectField('returntype',
                       label=_('Return type'),
                       has_arg=False,
                       names=('rtype',),
                       bodyrolename='class'),
    ]

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

        modname = self.options.get('module', self.env.ref_context.get('comobject:module'))
        classname, fullname = (name_prefix.rstrip('.'), name_prefix + name) if name_prefix else ('', name)

        signode['module'] = modname
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
        modname = self.options.get('module', self.env.ref_context.get('comobject:module'))
        fullname = (modname and modname + '.' or '') + name_cls[0]
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['comobject']['objects']
            objects[fullname] = (self.env.docname, self.objtype)

        indextext = self.get_index_text(modname, name_cls)
        if indextext:
            self.indexnode['entries'].append(('single', indextext, fullname, '', None))

    def before_content(self):
        prefix = None
        if self.names:
            (fullname, name_prefix) = self.names[-1]
            if name_prefix:
                prefix = name_prefix.strip('.')
        if prefix:
            self.env.ref_context['comobject:class'] = prefix

    def after_content(self):
        self.env.ref_context['comobject:class'] = None


class ComObjectClassmember(ComObjectBase):
    def needs_arglist(self):
        return self.objtype.endswith('method')

    def get_signature_prefix(self, sig):
        return ''

    def get_index_text(self, modname, name_cls):
        name, cls = name_cls
        add_modules = self.env.config.add_module_names
        result = ''
        if self.objtype == 'method':
            clsname, methname = name.rsplit('.', 1)
            if modname and add_modules:
                result = _('{}() ({}.{} method)'.format(methname, modname, clsname))
            else:
                result = _('{}() ({} method)'.format(methname, clsname))

        return result


class ComObjectXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        refnode['comobject:module'] = env.ref_context.get('comobject:module')
        if not has_explicit_title:
            title = title.lstrip('.')

        if target[0] == '.':
            target = target[1:]
            refnode['refspecific'] = True
        return title, target


class ComObjectModuleIndex(Index):
    name = 'modindex'
    localname = _('ComObject Module Index')
    shortname = _('modules')

    def generate(self, docnames=None):
        return [], False


class ComObjectDomain(Domain):
    name = 'comobject'
    label = 'ComObject'
    object_types = {
        'method': ObjType(_('method'), 'meth'),
        'module': ObjType(_('module'), 'mod')
    }

    directives = {
        'method': ComObjectClassmember
    }
    roles = {
        'meth': ComObjectXRefRole(fix_parens=True),
        'mod': ComObjectXRefRole()
    }
    initial_data = {
        'objects': {},
        'modules': {},
    }
    indices = [
        ComObjectModuleIndex,
    ]

    def clear_doc(self, docname):
        for fullname, (fn, _l) in list(self.data['objects'].items()):
            if fn == docname:
                del self.data['objects'][fullname]
        for modname, (fn, _x, _x, _x) in list(self.data['modules'].items()):
            if fn == docname:
                del self.data['modules'][modname]

    def find_obj(self, name, type, searchmode=0):
        if name[-2:] == '()':
            name = name[:-2]

        if not name:
            return []

        objects = self.data['objects']
        matches = []

        newname = None
        if searchmode == 1:
            objtypes = list(self.object_types) if type is None else self.objtypes_for_role(type)
            if objtypes is not None:
                if not newname:
                    searchname = '.' + name
                    matches = [(oname, objects[oname]) for oname in objects
                                   if oname.endswith(searchname) and objects[oname][1] in objtypes]
        else:
            if name in objects:
                newname = name
        if newname is not None:
            matches.append((newname, objects[newname]))
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
            if type != 'module':
                yield (refname, refname, type, docname, refname, 1)

    def get_full_qualified_name(self, node):
        modname = node.get('comobject:module')
        target = node.get('reftarget')
        return None if target is None else '.'.join(filter(None, [modname, target]))


def setup(app):
    app.add_domain(ComObjectDomain)

    return {
        'version': 'builtin',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
