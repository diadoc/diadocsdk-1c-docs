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


# REs for Python signatures
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


class CComXrefMixin(object):
    def make_xref(self,
                  rolename,
                  domain,
                  target,
                  innernode=nodes.emphasis,
                  contnode=None,
                  env=None,
                  ):
        print('CComXrefMixin.make_xref')
        result = super(CComXrefMixin, self).make_xref(rolename, domain, target, innernode, contnode, env)
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
                   rolename,                  # type: unicode
                   domain,                    # type: unicode
                   target,                    # type: unicode
                   innernode=nodes.emphasis,  # type: nodes.Node
                   contnode=None,             # type: nodes.Node
                   env=None,                  # type: BuildEnvironment
                   ):
        print('CComXrefMixin.make_xrefs')
        delims = r'(\s*[\[\]\(\),](?:\s*or\s)?\s*|\s+or\s+)'
        delims_re = re.compile(delims)
        sub_targets = re.split(delims, target)

        split_contnode = contnode and contnode.astext() == target

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


class CComTypedField(CComXrefMixin, TypedField):
    def make_xref(self, rolename, domain, target, innernode=nodes.emphasis, contnode=None, env=None):
        print('CComTypedField.make_xref')
        if rolename == 'class' and target == 'None':
            rolename = 'obj'

        return super(CComTypedField, self).make_xref(rolename, domain, target, innernode, contnode, env)


class CComObject(ObjectDescription):
    option_spec = {
        'noindex': directives.flag,
        'module': directives.unchanged,
        'annotation': directives.unchanged
    }

    doc_field_types = [
        CComTypedField('parameter',
                       label=_('Parameters'),
                       names=('param', 'parameter', 'arg', 'argument', 'keyword', 'kwarg', 'kwparam'),
                       typerolename='class',
                       typenames=('paramtype', 'type'),
                       can_collapse=True),

        CComTypedField('variable',
                       label=_('Variables'),
                       rolename='obj',
                       names=('var', 'ivar', 'cvar'),
                       typerolename='class',
                       typenames=('vartype',),
                       can_collapse=True)
    ]

    allow_nesting = False

    def get_signature_prefix(self, sig):
        print('CComTypedField.get_signature_prefix')
        return ''

    def needs_arglist(self):
        print('CComTypedField.needs_arglist')
        return False

    def handle_signature(self, sig, signode):
        print('CComTypedField.handle_signature')
        m = py_sig_re.match(sig)
        if m is None:
            raise ValueError
        name_prefix, name, arglist, retann = m.groups()
        classname = self.env.ref_context.get('CCom:class')
        if classname:
            if name_prefix and name_prefix.startswith(classname):
                fullname = name_prefix + name
                name_prefix = name_prefix[len(classname):].lstrip('.')
            elif name_prefix:
                fullname = classname + '.' + name_prefix + name
            else:
                fullname = classname + '.' + name
        else:
            if name_prefix:
                classname = name_prefix.rstrip('.')
                fullname = name_prefix + name
            else:
                classname = ''
                fullname = name

        signode['class'] = classname
        signode['fullname'] = fullname

        sig_prefix = self.get_signature_prefix(sig)
        if sig_prefix:
            signode += addnodes.desc_annotation(sig_prefix, sig_prefix)

        if name_prefix:
            signode += addnodes.desc_addname(name_prefix, name_prefix)

        anno = self.options.get('annotation')

        signode += addnodes.desc_name(name, name)
        if not arglist:
            if self.needs_arglist():
                signode += addnodes.desc_parameterlist()
            if retann:
                signode += addnodes.desc_returns(retann, retann)
            if anno:
                signode += addnodes.desc_annotation(' ' + anno, ' ' + anno)
            return fullname, name_prefix

        _pseudo_parse_arglist(signode, arglist)
        if retann:
            signode += addnodes.desc_returns(retann, retann)
        if anno:
            signode += addnodes.desc_annotation(' ' + anno, ' ' + anno)
        return fullname, name_prefix

    def get_index_text(self, name):
        print('CComTypedField.get_index_text')
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls, sig, signode):
        print('CComTypedField.add_target_and_index')
        fullname = name_cls[0]
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['CCom']['objects']
            if fullname in objects:
                self.state_machine.reporter.warning(
                    'duplicate object description of %s, ' % fullname +
                    'other instance in ' +
                    self.env.doc2path(objects[fullname][0]) +
                    ', use :noindex: for one of them',
                    line=self.lineno)
            objects[fullname] = (self.env.docname, self.objtype)

        indextext = self.get_index_text(name_cls)
        if indextext:
            self.indexnode['entries'].append(('single', indextext,
                                              fullname, '', None))

    def before_content(self):
        print('CComTypedField.before_content')
        prefix = None
        if self.names:
            (fullname, name_prefix) = self.names[-1]
            if self.allow_nesting:
                prefix = fullname
            elif name_prefix:
                prefix = name_prefix.strip('.')
        if prefix:
            self.env.ref_context['CCom:class'] = prefix
            if self.allow_nesting:
                classes = self.env.ref_context.setdefault('CCom:classes', [])
                classes.append(prefix)

    def after_content(self):
        print('CComTypedField.after_content')
        classes = self.env.ref_context.setdefault('CCom:classes', [])
        if self.allow_nesting:
            try:
                classes.pop()
            except IndexError:
                pass
        self.env.ref_context['CCom:class'] = (classes[-1] if len(classes) > 0
                                              else None)


class CComClassmember(CComObject):
    def needs_arglist(self):
        print('CComClassmember.needs_arglist')
        return self.objtype.endswith('method')

    def get_signature_prefix(self, sig):
        print('CComClassmember.get_signature_prefix')
        return ''

    def get_index_text(self, name_cls):
        print('CComClassmember.get_index_text')
        name, cls = name_cls
        access_via = ''
        if self.objtype == 'method':
            access_via = '()'
        try:
            clsname, membername = name.rsplit('.', 1)
            result = _('{}{} ({} {})'.format(membername, access_via, clsname, self.objtype))
        except ValueError:
            result = _('{}{}'.format(name, access_via))

        print('CComClassmember.get_index_text({}) -> {}'.format(name_cls, result))
        return result


class CComDecoratorMixin(object):
    def handle_signature(self, sig, signode):
        print('CComDecoratorMixin.handle_signature')
        ret = super(CComDecoratorMixin, self).handle_signature(sig, signode)  # type: ignore
        signode.insert(0, addnodes.desc_addname('@', '@'))
        return ret

    def needs_arglist(self):
        print('CComDecoratorMixin.needs_arglist')
        return False


class CComDecoratorMethod(CComDecoratorMixin, CComClassmember):
    def run(self):
        print('CComDecoratorMethod.run')
        self.name = 'CCom:method'
        return CComClassmember.run(self)


class CComXRefRole(XRefRole, CComObject):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        print('CComXRefRole.process_link')
        refnode['CCom:class'] = env.ref_context.get('CCom:class')
        if not has_explicit_title:
            title = title.lstrip('.')    # only has a meaning for the target
            target = target.lstrip('~')  # only has a meaning for the title
            # if the first character is a tilde, don't display the module/class
            # parts of the contents
            if title[0:1] == '~':
                title = title[1:]
                dot = title.rfind('.')
                if dot != -1:
                    title = title[dot + 1:]
        if target[0] == '.':
            target = target[1:]
            refnode['refspecific'] = True
        return title, target


class CComDomain(Domain):
    name = 'CCom'
    label = 'ComObject'
    object_types = {
        'class':        ObjType(_('class'),     'class', 'exc', 'obj'),
        'method':       ObjType(_('method'),    'meth', 'func' 'obj'),
        'attribute':    ObjType(_('attribute'), 'attr', 'obj')
    }
    directives = {
        'method':          CComClassmember,
        'attribute':       CComClassmember
    }
    roles = {
        'func':  CComXRefRole(fix_parens=True),
        'attr':  CComXRefRole(),
        'meth':  CComXRefRole(fix_parens=True),
        'obj':   CComXRefRole()
    }
    initial_data = {
        'objects': {}
    }
    indices = []

    def clear_doc(self, docname):
        print('CComDomain.clear_doc({})'.format(docname))
        for fullname, (fn, _l) in list(self.data['objects'].items()):
            if fn == docname:
                print('\tdelete self.data["objects"][{}]'.format(fullname))
                del self.data['objects'][fullname]

    def merge_domaindata(self, docnames, otherdata):
        print('CComDomain.merge_domaindata')
        for fullname, (fn, objtype) in otherdata['objects'].items():
            if fn in docnames:
                self.data['objects'][fullname] = (fn, objtype)

    def find_obj(self, env, classname, name, type, searchmode=0):
        print('CComDomain.find_obj')
        if name[-2:] == '()':
            name = name[:-2]

        if not name:
            return []

        objects = self.data['objects']
        matches = []

        newname = None
        if searchmode == 1:
            if type is None:
                objtypes = list(self.object_types)
            else:
                objtypes = self.objtypes_for_role(type)
            if objtypes is not None:
                if classname:
                    fullname = classname + '.' + name
                    if fullname in objects and objects[fullname][1] in objtypes:
                        newname = fullname
                if not newname:
                    if name in objects and objects[name][1] in objtypes:
                        newname = name
                    else:
                        searchname = '.' + name
                        matches = [(oname, objects[oname]) for oname in objects
                                   if oname.endswith(searchname) and
                                   objects[oname][1] in objtypes]
        else:
            if name in objects:
                newname = name
            elif classname and classname + '.' + name in objects:
                newname = classname + '.' + name
            elif type in ('func', 'meth') and '.' not in name and 'object.' + name in objects:
                newname = 'object.' + name
        if newname is not None:
            matches.append((newname, objects[newname]))
        print('CComDomain.find_obj({}, {}, {}, {}, {}) -> {}'.format(env, classname, name, type, searchmode, matches))
        return matches

    def resolve_xref(self, env, fromdocname, builder, type, target, node, contnode):
        print('CComDomain.resolve_xref')
        clsname = node.get('CCom:class')
        searchmode = node.hasattr('refspecific') and 1 or 0
        matches = self.find_obj(env, clsname, target, type, searchmode)
        if not matches:
            return None
        elif len(matches) > 1:
            message = 'more than one target found for cross-reference {}: {}'.format(target.repr(), ', '.join(match[0] for match in matches))
            logger.warning(message, type='ref', subtype='ccom', location=node)
        name, obj = matches[0]

        return make_refnode(builder, fromdocname, obj[0], name, contnode, name)

    def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
        print('CComDomain.resolve_any_xref')
        clsname = node.get('CCom:class')
        results = []
        matches = self.find_obj(env, clsname, target, None, 1)
        for name, obj in matches:
            results.append(('CCom:' + self.role_for_objtype(obj[1]),
                            make_refnode(builder, fromdocname, obj[0], name, contnode, name)))
        return results

    def get_objects(self):
        print('CComDomain.get_objects')
        for refname, (docname, type) in iteritems(self.data['objects']):
            yield (refname, refname, type, docname, refname, 1)

    def get_full_qualified_name(self, node):
        print('CComDomain.get_full_qualified_name')
        clsname = node.get('CCom:class')
        target = node.get('reftarget')
        return None if target is None \
                    else '.'.join(filter(None, [clsname, target]))


def setup(app):
    print('SETUP!!!!')
    app.add_domain(CComDomain)

    return {
        'version': 'builtin',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
