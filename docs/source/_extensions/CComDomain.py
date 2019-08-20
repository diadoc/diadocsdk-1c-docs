# -*- coding: utf-8 -*-
"""
    sphinx.domains.python
    ~~~~~~~~~~~~~~~~~~~~~

    The Python domain.

    :copyright: Copyright 2007-2019 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

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
class ComObjectXrefMixin(object):
    def make_xref(self,
                  rolename,                  # type: unicode
                  domain,                    # type: unicode
                  target,                    # type: unicode
                  innernode=nodes.emphasis,  # type: nodes.Node
                  contnode=None,             # type: nodes.Node
                  env=None,                  # type: BuildEnvironment
                  ):
        # type: (...) -> nodes.Node
        result = super(ComObjectXrefMixin, self).make_xref(rolename, domain, target,  # type: ignore
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


class ComObjectField(ComObjectXrefMixin, Field):
    def make_xref(self, rolename, domain, target,
                  innernode=nodes.emphasis, contnode=None, env=None):
        # type: (unicode, unicode, unicode, nodes.Node, nodes.Node, BuildEnvironment) ->  nodes.Node  # NOQA
        if rolename == 'class' and target == 'None':
            # None is not a type, so use obj role instead.
            rolename = 'obj'

        return super(ComObjectField, self).make_xref(rolename, domain, target,
                                              innernode, contnode, env)


class ComObjectGroupedField(ComObjectXrefMixin, GroupedField):
    pass


class ComObjectTypedField(ComObjectXrefMixin, TypedField):
    def make_xref(self, rolename, domain, target,
                  innernode=nodes.emphasis, contnode=None, env=None):
        # type: (unicode, unicode, unicode, nodes.Node, nodes.Node, BuildEnvironment) ->  nodes.Node  # NOQA
        if rolename == 'class' and target == 'None':
            # None is not a type, so use obj role instead.
            rolename = 'obj'

        return super(ComObjectTypedField, self).make_xref(rolename, domain, target,
                                                   innernode, contnode, env)


class ComObjectBase(ObjectDescription):
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
        ComObjectTypedField('parameter', label=_('Parameters'),
                     names=('param', 'parameter', 'arg', 'argument',
                            'keyword', 'kwarg', 'kwparam'),
                     typerolename='class', typenames=('paramtype', 'type'),
                     can_collapse=True),
        ComObjectTypedField('variable', label=_('Variables'), rolename='obj',
                     names=('var', 'ivar', 'cvar'),
                     typerolename='class', typenames=('vartype',),
                     can_collapse=True),
        ComObjectGroupedField('exceptions', label=_('Raises'), rolename='exc',
                       names=('raises', 'raise', 'exception', 'except'),
                       can_collapse=True),
        Field('returnvalue', label=_('Returns'), has_arg=False,
              names=('returns', 'return')),
        ComObjectField('returntype', label=_('Return type'), has_arg=False,
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
            'module', self.env.ref_context.get('comobject:module'))
        classname = self.env.ref_context.get('comobject:class')
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
                'module', self.env.ref_context.get('comobject:module'))
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

    def get_index_text(self, modname, name):
        # type: (unicode, unicode) -> unicode
        """Return the text for the index entry of the object."""
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls, sig, signode):
        # type: (unicode, unicode, addnodes.desc_signature) -> None
        print('ComObjectBase.add_target_and_index({}, {}, {})'.format(name_cls, sig, signode))
        modname = self.options.get(
            'module', self.env.ref_context.get('comobject:module'))
        fullname = (modname and modname + '.' or '') + name_cls[0]
        # note target
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['comobject']['objects']
            if fullname in objects:
                self.state_machine.reporter.warning(
                    'duplicate object description of %s, ' % fullname +
                    'other instance in ' +
                    self.env.doc2path(objects[fullname][0]) +
                    ', use :noindex: for one of them',
                    line=self.lineno)
            objects[fullname] = (self.env.docname, self.objtype)

        indextext = self.get_index_text(modname, name_cls)
        if indextext:
            self.indexnode['entries'].append(('single', indextext,
                                              fullname, '', None))

    def before_content(self):
        # type: () -> None
        """Handle object nesting before content

        :py:class:`ComObjectBase` represents Python language constructs. For
        constructs that are nestable, such as a Python classes, this method will
        build up a stack of the nesting heirarchy so that it can be later
        de-nested correctly, in :py:meth:`after_content`.

        For constructs that aren't nestable, the stack is bypassed, and instead
        only the most recent object is tracked. This object prefix name will be
        removed with :py:meth:`after_content`.
        """
        prefix = None
        if self.names:
            # fullname and name_prefix come from the `handle_signature` method.
            # fullname represents the full object name that is constructed using
            # object nesting and explicit prefixes. `name_prefix` is the
            # explicit prefix given in a signature
            (fullname, name_prefix) = self.names[-1]
            if self.allow_nesting:
                prefix = fullname
            elif name_prefix:
                prefix = name_prefix.strip('.')
        if prefix:
            self.env.ref_context['comobject:class'] = prefix
            if self.allow_nesting:
                classes = self.env.ref_context.setdefault('comobject:classes', [])
                classes.append(prefix)
        if 'module' in self.options:
            modules = self.env.ref_context.setdefault('comobject:modules', [])
            modules.append(self.env.ref_context.get('comobject:module'))
            self.env.ref_context['comobject:module'] = self.options['module']

    def after_content(self):
        # type: () -> None
        """Handle object de-nesting after content

        If this class is a nestable object, removing the last nested class prefix
        ends further nesting in the object.

        If this class is not a nestable object, the list of classes should not
        be altered as we didn't affect the nesting levels in
        :py:meth:`before_content`.
        """
        classes = self.env.ref_context.setdefault('py:classes', [])
        if self.allow_nesting:
            try:
                classes.pop()
            except IndexError:
                pass
        self.env.ref_context['py:class'] = (classes[-1] if len(classes) > 0
                                            else None)
        if 'module' in self.options:
            modules = self.env.ref_context.setdefault('py:modules', [])
            if modules:
                self.env.ref_context['comobject:module'] = modules.pop()
            else:
                self.env.ref_context.pop('comobject:module')


class ComObjectModulelevel(ComObjectBase):
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


class ComObjectClasslike(ComObjectBase):
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
        elif self.objtype == 'exception':
            return name_cls[0]
        else:
            return ''


class ComObjectClassmember(ComObjectBase):
    """
    Description of a class member (methods, attributes).
    """

    def needs_arglist(self):
        # type: () -> bool
        return self.objtype.endswith('method')

    def get_signature_prefix(self, sig):
        # type: (unicode) -> unicode
        if self.objtype == 'staticmethod':
            return 'static '
        elif self.objtype == 'classmethod':
            return 'classmethod '
        return ''

    def get_index_text(self, modname, name_cls):
        # type: (unicode, unicode) -> unicode
        name, cls = name_cls
        add_modules = self.env.config.add_module_names
        if self.objtype == 'method':
            try:
                clsname, methname = name.rsplit('.', 1)
            except ValueError:
                if modname:
                    result = _('%s() (in module %s)') % (name, modname)
                    print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                    return result
                else:
                    result = '%s()' % name
                    print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                    return result
            if modname and add_modules:
                result = _('%s() (%s.%s method)') % (methname, modname, clsname)
                print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                return result
            else:
                result = _('%s() (%s method)') % (methname, clsname)
                print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                return result
        elif self.objtype == 'staticmethod':
            try:
                clsname, methname = name.rsplit('.', 1)
            except ValueError:
                if modname:
                    result = _('%s() (in module %s)') % (name, modname)
                    print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                    return result
                else:
                    result = '%s()' % name
                    print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                    return result
            if modname and add_modules:
                result = _('%s() (%s.%s static method)') % (methname, modname,
                                                          clsname)
                print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                return result
            else:
                result = _('%s() (%s static method)') % (methname, clsname)
                print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                return result
            if modname:
                result = _('%s() (%s.%s class method)') % (methname, modname,
                                                         clsname)
                print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                return result
            else:
                result = _('%s() (%s class method)') % (methname, clsname)
                print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                return result
        elif self.objtype == 'attribute':
            try:
                clsname, attrname = name.rsplit('.', 1)
            except ValueError:
                if modname:
                    result = _('%s (in module %s)') % (name, modname)
                    print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                    return result
                else:
                    result = name
                    print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                    return result
            if modname and add_modules:
                result = _('%s (%s.%s attribute)') % (attrname, modname, clsname)
                print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                return result
            else:
                result = _('%s (%s attribute)') % (attrname, clsname)
                print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
                return result
        else:
            result = ''
            print('ComObjectClassmember.get_index_text({}) -> {}'.format(name_cls, result))
            return result


class ComObjectDecoratorMixin(object):
    """
    Mixin for decorator directives.
    """
    def handle_signature(self, sig, signode):
        # type: (unicode, addnodes.desc_signature) -> Tuple[unicode, unicode]
        ret = super(ComObjectDecoratorMixin, self).handle_signature(sig, signode)  # type: ignore
        signode.insert(0, addnodes.desc_addname('@', '@'))
        return ret

    def needs_arglist(self):
        # type: () -> bool
        return False


class ComObjectDecoratorFunction(ComObjectDecoratorMixin, ComObjectModulelevel):
    """
    Directive to mark functions meant to be used as decorators.
    """
    def run(self):
        # type: () -> List[nodes.Node]
        # a decorator function is a function after all
        self.name = 'comobject:function'
        return ComObjectModulelevel.run(self)


class ComObjectDecoratorMethod(ComObjectDecoratorMixin, ComObjectClassmember):
    """
    Directive to mark methods meant to be used as decorators.
    """
    def run(self):
        # type: () -> List[nodes.Node]
        self.name = 'comobject:method'
        return ComObjectClassmember.run(self)


class ComObjectModule(SphinxDirective):
    """
    Directive to mark description of a new module.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'platform': lambda x: x,
        'synopsis': lambda x: x,
        'noindex': directives.flag,
        'deprecated': directives.flag,
    }

    def run(self):
        # type: () -> List[nodes.Node]
        modname = self.arguments[0].strip()
        noindex = 'noindex' in self.options
        self.env.ref_context['comobject:module'] = modname
        ret = []
        if not noindex:
            self.env.domaindata['comobject']['modules'][modname] = (self.env.docname,
                                                             self.options.get('synopsis', ''),
                                                             self.options.get('platform', ''),
                                                             'deprecated' in self.options)
            # make a duplicate entry in 'objects' to facilitate searching for
            # the module in ComObjectDomain.find_obj()
            self.env.domaindata['comobject']['objects'][modname] = (self.env.docname, 'module')
            targetnode = nodes.target('', '', ids=['module-' + modname],
                                      ismod=True)
            self.state.document.note_explicit_target(targetnode)
            # the platform and synopsis aren't printed; in fact, they are only
            # used in the modindex currently
            ret.append(targetnode)
            indextext = _('%s (module)') % modname
            inode = addnodes.index(entries=[('single', indextext,
                                             'module-' + modname, '', None)])
            ret.append(inode)
        return ret


class ComObjectCurrentModule(SphinxDirective):

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}  # type: Dict

    def run(self):
        # type: () -> List[nodes.Node]
        modname = self.arguments[0].strip()
        if modname == 'None':
            self.env.ref_context.pop('comobject:module', None)
        else:
            self.env.ref_context['comobject:module'] = modname
        return []


class ComObjectXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        # type: (BuildEnvironment, nodes.Node, bool, unicode, unicode) -> Tuple[unicode, unicode]  # NOQA
        refnode['comobject:module'] = env.ref_context.get('comobject:module')
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


class ComObjectModuleIndex(Index):
    name = 'modindex'
    localname = _('ComObject Module Index')
    shortname = _('modules')

    def generate(self, docnames=None):
        # type: (Iterable[unicode]) -> Tuple[List[Tuple[unicode, List[List[Union[unicode, int]]]]], bool]  # NOQA
        content = {}  # type: Dict[unicode, List]
        # list of prefixes to ignore
        ignores = None  # type: List[unicode]
        ignores = self.domain.env.config['modindex_common_prefix']  # type: ignore
        ignores = sorted(ignores, key=len, reverse=True)
        # list of all modules, sorted by module name
        modules = sorted(iteritems(self.domain.data['modules']),
                         key=lambda x: x[0].lower())
        # sort out collapsable modules
        prev_modname = ''
        num_toplevels = 0
        for modname, (docname, synopsis, platforms, deprecated) in modules:
            if docnames and docname not in docnames:
                continue

            for ignore in ignores:
                if modname.startswith(ignore):
                    modname = modname[len(ignore):]
                    stripped = ignore
                    break
            else:
                stripped = ''

            # we stripped the whole module name?
            if not modname:
                modname, stripped = stripped, ''

            entries = content.setdefault(modname[0].lower(), [])

            package = modname.split('.')[0]
            if package != modname:
                if prev_modname == package:
                    if entries:
                        entries[-1][1] = 1
                elif not prev_modname.startswith(package):
                    entries.append([stripped + package, 1, '', '', '', '', ''])
                subtype = 2
            else:
                num_toplevels += 1
                subtype = 0

            qualifier = deprecated and _('Deprecated') or ''
            entries.append([stripped + modname, subtype, docname,
                            'module-' + stripped + modname, platforms,
                            qualifier, synopsis])
            prev_modname = modname

        collapse = len(modules) - num_toplevels < num_toplevels
        sorted_content = sorted(iteritems(content))

        return sorted_content, collapse


class ComObjectDomain(Domain):
    """Python language domain."""
    name = 'comobject'
    label = 'ComObject'
    object_types = {
        'function':     ObjType(_('function'),      'func', 'obj'),
        'data':         ObjType(_('data'),          'data', 'obj'),
        'class':        ObjType(_('class'),         'class', 'exc', 'obj'),
        'exception':    ObjType(_('exception'),     'exc', 'class', 'obj'),
        'method':       ObjType(_('method'),        'meth', 'obj'),
        'classmethod':  ObjType(_('class method'),  'meth', 'obj'),
        'staticmethod': ObjType(_('static method'), 'meth', 'obj'),
        'attribute':    ObjType(_('attribute'),     'attr', 'obj'),
        'module':       ObjType(_('module'),        'mod', 'obj'),
    }  # type: Dict[unicode, ObjType]

    directives = {
        'function':        ComObjectModulelevel,
        'data':            ComObjectModulelevel,
        'class':           ComObjectClasslike,
        'exception':       ComObjectClasslike,
        'method':          ComObjectClassmember,
        'classmethod':     ComObjectClassmember,
        'staticmethod':    ComObjectClassmember,
        'attribute':       ComObjectClassmember,
        'module':          ComObjectModule,
        'currentmodule':   ComObjectCurrentModule,
        'decorator':       ComObjectDecoratorFunction,
        'decoratormethod': ComObjectDecoratorMethod,
    }
    roles = {
        'data':  ComObjectXRefRole(),
        'exc':   ComObjectXRefRole(),
        'func':  ComObjectXRefRole(fix_parens=True),
        'class': ComObjectXRefRole(),
        'const': ComObjectXRefRole(),
        'attr':  ComObjectXRefRole(),
        'meth':  ComObjectXRefRole(fix_parens=True),
        'mod':   ComObjectXRefRole(),
        'obj':   ComObjectXRefRole(),
    }
    initial_data = {
        'objects': {},  # fullname -> docname, objtype
        'modules': {},  # modname -> docname, synopsis, platform, deprecated
    }  # type: Dict[unicode, Dict[unicode, Tuple[Any]]]
    indices = [
        ComObjectModuleIndex,
    ]

    def clear_doc(self, docname):
        # type: (unicode) -> None
        for fullname, (fn, _l) in list(self.data['objects'].items()):
            if fn == docname:
                del self.data['objects'][fullname]
        for modname, (fn, _x, _x, _x) in list(self.data['modules'].items()):
            if fn == docname:
                del self.data['modules'][modname]

    def merge_domaindata(self, docnames, otherdata):
        # type: (List[unicode], Dict) -> None
        # XXX check duplicates?
        for fullname, (fn, objtype) in otherdata['objects'].items():
            if fn in docnames:
                self.data['objects'][fullname] = (fn, objtype)
        for modname, data in otherdata['modules'].items():
            if data[0] in docnames:
                self.data['modules'][modname] = data

    def find_obj(self, env, modname, name, type, searchmode=0):
        # type: (BuildEnvironment, unicode, unicode, unicode, unicode, int) -> List[Tuple[unicode, Any]]  # NOQA
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
                if modname:
                    fullname = modname + '.' +  name
                    if fullname in objects and objects[fullname][1] in objtypes:
                        newname = fullname
                if not newname:
                    if modname and modname + '.' + name in objects and \
                       objects[modname + '.' + name][1] in objtypes:
                        newname = modname + '.' + name
                    elif name in objects and objects[name][1] in objtypes:
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
            elif type == 'mod':
                # only exact matches allowed for modules
                return []
            elif modname and modname + '.' + name in objects:
                newname = modname + '.' + name
            # special case: builtin exceptions have module "exceptions" set
            elif type == 'exc' and '.' not in name and \
                    'exceptions.' + name in objects:
                newname = 'exceptions.' + name
            # special case: object methods
            elif type in ('func', 'meth') and '.' not in name and \
                    'object.' + name in objects:
                newname = 'object.' + name
        if newname is not None:
            matches.append((newname, objects[newname]))
        return matches

    def resolve_xref(self, env, fromdocname, builder, type, target, node, contnode):
        modname = node.get('comobject:module')
        searchmode = node.hasattr('refspecific') and 1 or 0
        matches = self.find_obj(env, modname, target,
                                type, searchmode)
        if not matches:
            return None
        elif len(matches) > 1:
            logger.warning(__('more than one target found for cross-reference %r: %s'),
                           target, ', '.join(match[0] for match in matches),
                           type='ref', subtype='comobject', location=node)
        name, obj = matches[0]

        if obj[1] == 'module':
            return self._make_module_refnode(builder, fromdocname, name,
                                             contnode)
        else:
            return make_refnode(builder, fromdocname, obj[0], name,
                                contnode, name)

    def resolve_any_xref(self, env, fromdocname, builder, target,
                         node, contnode):
        modname = node.get('comobject:module')
        results = []

        matches = self.find_obj(env, modname, target, None, 1)
        for name, obj in matches:
            if obj[1] == 'module':
                results.append(('comobject:mod',
                                self._make_module_refnode(builder, fromdocname,
                                                          name, contnode)))
            else:
                results.append(('comobject:' + self.role_for_objtype(obj[1]),
                                make_refnode(builder, fromdocname, obj[0], name,
                                             contnode, name)))
        return results

    def _make_module_refnode(self, builder, fromdocname, name, contnode):
        docname, synopsis, platform, deprecated = self.data['modules'][name]
        title = name
        if synopsis:
            title += ': ' + synopsis
        if deprecated:
            title += _(' (deprecated)')
        if platform:
            title += ' (' + platform + ')'
        return make_refnode(builder, fromdocname, docname,
                            'module-' + name, contnode, title)

    def get_objects(self):
        for modname, info in iteritems(self.data['modules']):
            yield (modname, modname, 'module', info[0], 'module-' + modname, 0)
        for refname, (docname, type) in iteritems(self.data['objects']):
            if type != 'module':
                yield (refname, refname, type, docname, refname, 1)

    def get_full_qualified_name(self, node):
        modname = node.get('comobject:module')
        target = node.get('reftarget')
        if target is None:
            return None
        else:
            return '.'.join(filter(None, [modname, target]))


def setup(app):
    app.add_domain(ComObjectDomain)

    return {
        'version': 'builtin',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
