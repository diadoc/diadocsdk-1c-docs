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
}  # Dict[unicode, unicode]

locale.pairindextypes = DeprecatedDict(
    pairindextypes,
    'sphinx.locale.pairindextypes is deprecated. '
    'Please use sphinx.domains.python.pairindextypes instead.',
    RemovedInSphinx30Warning
)


def _pseudo_parse_arglist(signode, arglist):
    # type: (addnodes.desc_signature, unicode) -> None
    """"Parse" a list of arguments separated by commas.

    Arguments can have "optional" annotations given by enclosing them in
    brackets.  Currently, this will split at any comma, even if it's inside a
    string literal (e.g. default argument value).
    """
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
        # if there are too few or too many elements on the stack, just give up
        # and treat the whole argument list as one argument, discarding the
        # already partially populated paramlist node
        signode += addnodes.desc_parameterlist()
        signode[-1] += addnodes.desc_parameter(arglist, arglist)
    else:
        signode += paramlist


# This override allows our inline type specifiers to behave like :class: link
# when it comes to handling "." and "~" prefixes.
class CComXrefMixin(object):
    def make_xref(self,
                  rolename,                  # type: unicode
                  domain,                    # type: unicode
                  target,                    # type: unicode
                  innernode=nodes.emphasis,  # type: nodes.Node
                  contnode=None,             # type: nodes.Node
                  env=None,                  # type: BuildEnvironment
                  ):
        # type: (...) -> nodes.Node
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


class CComField(CComXrefMixin, Field):
    def make_xref(self, rolename, domain, target,
                  innernode=nodes.emphasis, contnode=None, env=None):
        # type: (unicode, unicode, unicode, nodes.Node, nodes.Node, BuildEnvironment) ->  nodes.Node  # NOQA
        if rolename == 'class' and target == 'None':
            # None is not a type, so use obj role instead.
            rolename = 'obj'

        return super(CComField, self).make_xref(rolename, domain, target,
                                              innernode, contnode, env)


class CComGroupedField(CComXrefMixin, GroupedField):
    pass


class CComTypedField(CComXrefMixin, TypedField):
    def make_xref(self, rolename, domain, target,
                  innernode=nodes.emphasis, contnode=None, env=None):
        # type: (unicode, unicode, unicode, nodes.Node, nodes.Node, BuildEnvironment) ->  nodes.Node  # NOQA
        if rolename == 'class' and target == 'None':
            # None is not a type, so use obj role instead.
            rolename = 'obj'

        return super(CComTypedField, self).make_xref(rolename, domain, target, innernode, contnode, env)


class CComTypedField(ObjectDescription):
    """
    Description of a general Python object.

    :cvar allow_nesting: Class is an object that allows for nested namespaces
    :vartype allow_nesting: bool
    """
    option_spec = {
        'noindex': directives.flag,
        'module': directives.unchanged,
        'annotation': directives.unchanged,
    }

    doc_field_types = [
        CComTypedField('parameter', label=_('Parameters'),
                     names=('param', 'parameter', 'arg', 'argument',
                            'keyword', 'kwarg', 'kwparam'),
                     typerolename='class', typenames=('paramtype', 'type'),
                     can_collapse=True),
        CComTypedField('variable', label=_('Variables'), rolename='obj',
                     names=('var', 'ivar', 'cvar'),
                     typerolename='class', typenames=('vartype',),
                     can_collapse=True),
        CComGroupedField('exceptions', label=_('Raises'), rolename='exc',
                       names=('raises', 'raise', 'exception', 'except'),
                       can_collapse=True),
        Field('returnvalue', label=_('Returns'), has_arg=False,
              names=('returns', 'return')),
        CComField('returntype', label=_('Return type'), has_arg=False,
                names=('rtype',), bodyrolename='class'),
    ]

    allow_nesting = False

    def get_signature_prefix(self, sig):
        # type: (unicode) -> unicode
        """May return a prefix to put before the object name in the
        signature.
        """
        return ''

    def needs_arglist(self):
        # type: () -> bool
        """May return true if an empty argument list is to be generated even if
        the document contains none.
        """
        return False

    def handle_signature(self, sig, signode):
        # type: (unicode, addnodes.desc_signature) -> Tuple[unicode, unicode]
        """Transform a Python signature into RST nodes.

        Return (fully qualified name of the thing, classname if any).

        If inside a class, the current class name is handled intelligently:
        * it is stripped from the displayed name if present
        * it is added to the full name (return value) if not present
        """
        m = py_sig_re.match(sig)
        if m is None:
            raise ValueError
        name_prefix, name, arglist, retann = m.groups()

        # determine module and class name (if applicable), as well as full name
        modname = self.options.get(
            'module', self.env.ref_context.get('CCom:module'))
        classname = self.env.ref_context.get('CCom:class')
        if classname:
            add_module = False
            if name_prefix and name_prefix.startswith(classname):
                fullname = name_prefix + name
                # class name is given again in the signature
                name_prefix = name_prefix[len(classname):].lstrip('.')
            elif name_prefix:
                # class name is given in the signature, but different
                # (shouldn't happen)
                fullname = classname + '.' + name_prefix + name
            else:
                # class name is not given in the signature
                fullname = classname + '.' + name
        else:
            add_module = True
            if name_prefix:
                classname = name_prefix.rstrip('.')
                fullname = name_prefix + name
            else:
                classname = ''
                fullname = name

        signode['module'] = modname
        signode['class'] = classname
        signode['fullname'] = fullname

        sig_prefix = self.get_signature_prefix(sig)
        if sig_prefix:
            signode += addnodes.desc_annotation(sig_prefix, sig_prefix)

        if name_prefix:
            signode += addnodes.desc_addname(name_prefix, name_prefix)
        # exceptions are a special case, since they are documented in the
        # 'exceptions' module.
        elif add_module and self.env.config.add_module_names:
            modname = self.options.get(
                'module', self.env.ref_context.get('CCom:module'))
            if modname and modname != 'exceptions':
                nodetext = modname + '.'
                signode += addnodes.desc_addname(nodetext, nodetext)

        anno = self.options.get('annotation')

        signode += addnodes.desc_name(name, name)
        if not arglist:
            if self.needs_arglist():
                # for callables, add an empty parameter list
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
        # type: (unicode) -> unicode
        """Return the text for the index entry of the object."""
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls, sig, signode):
        # type: (unicode, unicode, addnodes.desc_signature) -> None
        fullname = name_cls[0]
        # note target
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
        # type: () -> None
        """Handle object nesting before content

        :CCom:class:`CComTypedField` represents Python language constructs. For
        constructs that are nestable, such as a Python classes, this method will
        build up a stack of the nesting heirarchy so that it can be later
        de-nested correctly, in :CCom:meth:`after_content`.

        For constructs that aren't nestable, the stack is bypassed, and instead
        only the most recent object is tracked. This object prefix name will be
        removed with :CCom:meth:`after_content`.
        """
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
        if 'module' in self.options:
            modules = self.env.ref_context.setdefault('CCom:modules', [])
            modules.append(self.env.ref_context.get('CCom:module'))
            self.env.ref_context['CCom:module'] = self.options['module']

    def after_content(self):
        # type: () -> None
        """Handle object de-nesting after content

        If this class is a nestable object, removing the last nested class prefix
        ends further nesting in the object.

        If this class is not a nestable object, the list of classes should not
        be altered as we didn't affect the nesting levels in
        :CCom:meth:`before_content`.
        """
        classes = self.env.ref_context.setdefault('CCom:classes', [])
        if self.allow_nesting:
            try:
                classes.pop()
            except IndexError:
                pass
        self.env.ref_context['CCom:class'] = (classes[-1] if len(classes) > 0
                                                          else None)
        if 'module' in self.options:
            modules = self.env.ref_context.setdefault('CCom:modules', [])
            if modules:
                self.env.ref_context['CCom:module'] = modules.pop()
            else:
                self.env.ref_context.pop('CCom:module')


class CComModulelevel(CComTypedField):
    """
    Description of an object on module level (functions, data).
    """

    def needs_arglist(self):
        # type: () -> bool
        return self.objtype == 'function'

    def get_index_text(self, modname, name_cls):
        # type: (unicode, unicode) -> unicode
        if self.objtype == 'function':
            if not modname:
                return _('%s() (built-in function)') % name_cls[0]
            return _('%s() (in module %s)') % (name_cls[0], modname)
        elif self.objtype == 'data':
            if not modname:
                return _('%s (built-in variable)') % name_cls[0]
            return _('%s (in module %s)') % (name_cls[0], modname)
        else:
            return ''


class CComClasslike(CComTypedField):
    """
    Description of a class-like object (classes, interfaces, exceptions).
    """

    allow_nesting = True

    def get_signature_prefix(self, sig):
        # type: (unicode) -> unicode
        return self.objtype + ' '

    def get_index_text(self, modname, name_cls):
        # type: (unicode, unicode) -> unicode
        if self.objtype == 'class':
            if not modname:
                return _('%s (built-in class)') % name_cls[0]
            return _('%s (class in %s)') % (name_cls[0], modname)
        # elif self.objtype == 'exception':
        #     return name_cls[0]
        else:
            return ''


class CComClassmember(CComTypedField):
    """
    Description of a class member (methods, attributes).
    """

    def needs_arglist(self):
        # type: () -> bool
        return self.objtype.endswith('method')

    def get_signature_prefix(self, sig):
        return ''

    def get_index_text(self, name_cls):
        # type: (unicode, unicode) -> unicode
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
    """
    Mixin for decorator directives.
    """
    def handle_signature(self, sig, signode):
        # type: (unicode, addnodes.desc_signature) -> Tuple[unicode, unicode]
        ret = super(CComDecoratorMixin, self).handle_signature(sig, signode)  # type: ignore
        signode.insert(0, addnodes.desc_addname('@', '@'))
        return ret

    def needs_arglist(self):
        # type: () -> bool
        return False


class CComDecoratorMethod(CComDecoratorMixin, CComClassmember):
    """
    Directive to mark methods meant to be used as decorators.
    """
    def run(self):
        # type: () -> List[nodes.Node]
        self.name = 'CCom:method'
        return CComClassmember.run(self)


class CComXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        # type: (BuildEnvironment, nodes.Node, bool, unicode, unicode) -> Tuple[unicode, unicode]  # NOQA
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
        # if the first character is a dot, search more specific namespaces first
        # else search builtins first
        if target[0:1] == '.':
            target = target[1:]
            refnode['refspecific'] = True
        return title, target



class CComDomain(Domain):
    """Python language domain."""
    name = 'CCom'
    label = 'ComObject'
    object_types = {
        'class':        ObjType(_('class'),     'class', 'exc', 'obj'),
        'method':       ObjType(_('method'),    'meth', 'func' 'obj'),
        'attribute':    ObjType(_('attribute'), 'attr', 'obj')
    }  # type: Dict[unicode, ObjType]

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
        'objects': {}  # fullname -> docname, objtype
    }  # type: Dict[unicode, Dict[unicode, Tuple[Any]]]
    indices = [
       # ComObjectModuleIndex,
    ]

    def clear_doc(self, docname):
        # type: (unicode) -> None
        for fullname, (fn, _l) in list(self.data['objects'].items()):
            if fn == docname:
                del self.data['objects'][fullname]

    def merge_domaindata(self, docnames, otherdata):
        # type: (List[unicode], Dict) -> None
        # XXX check duplicates?
        for fullname, (fn, objtype) in otherdata['objects'].items():
            if fn in docnames:
                self.data['objects'][fullname] = (fn, objtype)

    def find_obj(self, env, classname, name, type, searchmode=0):
        # type: (BuildEnvironment, unicode, unicode, unicode, int) -> List[Tuple[unicode, Any]]  # NOQA
        """Find a Python object for "name", perhaps using the given module
        and/or classname.  Returns a list of (name, object entry) tuples.
        """
        # skip parens
        if name[-2:] == '()':
            name = name[:-2]

        if not name:
            return []

        objects = self.data['objects']
        matches = []  # type: List[Tuple[unicode, Any]]

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
                        # "fuzzy" searching mode
                        searchname = '.' + name
                        matches = [(oname, objects[oname]) for oname in objects
                                   if oname.endswith(searchname) and
                                   objects[oname][1] in objtypes]
        else:
            # NOTE: searching for exact match, object type is not considered
            if name in objects:
                newname = name
            elif classname and classname + '.' + name in objects:
                newname = classname + '.' + name
            elif type in ('func', 'meth') and '.' not in name and \
                    'object.' + name in objects:
                newname = 'object.' + name
        if newname is not None:
            matches.append((newname, objects[newname]))
        return matches

    def resolve_xref(self, env, fromdocname, builder, type, target, node, contnode):
        # type: (BuildEnvironment, unicode, Builder, unicode, unicode, nodes.Node, nodes.Node) -> nodes.Node  # NOQA
        clsname = node.get('CCom:class')
        searchmode = node.hasattr('refspecific') and 1 or 0
        matches = self.find_obj(env, clsname, target, type, searchmode)
        if not matches:
            return None
        elif len(matches) > 1:
            logger.warning(__('more than one target found for cross-reference %r: %s'),
                           target, ', '.join(match[0] for match in matches),
                           type='ref', subtype='ccom', location=node)
        name, obj = matches[0]

        return make_refnode(builder, fromdocname, obj[0], name, contnode, name)

    def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
        # type: (BuildEnvironment, unicode, Builder, unicode, nodes.Node, nodes.Node) -> List[Tuple[unicode, nodes.Node]]  # NOQA
        clsname = node.get('CCom:class')
        results = []  # type: List[Tuple[unicode, nodes.Node]]

        # always search in "refspecific" mode with the :any: role
        matches = self.find_obj(env, modname, clsname, target, None, 1)
        for name, obj in matches:
            results.append(('CCom:' + self.role_for_objtype(obj[1]),
                            make_refnode(builder, fromdocname, obj[0], name, contnode, name)))
        return results


    def get_objects(self):
        # type: () -> Iterator[Tuple[unicode, unicode, unicode, unicode, unicode, int]]
        for refname, (docname, type) in iteritems(self.data['objects']):
            yield (refname, refname, type, docname, refname, 1)

    def get_full_qualified_name(self, node):
        # type: (nodes.Node) -> unicode
        clsname = node.get('CCom:class')
        target = node.get('reftarget')
        if target is None:
            return None
        else:
            return '.'.join(filter(None, [modname, clsname, target]))


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_domain(CComDomain)

    return {
        'version': 'builtin',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
