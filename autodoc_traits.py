"""
sphinx.ext.autodoc extension for classes with configurable traits.

The code here is similar to the official code example in
https://www.sphinx-doc.org/en/master/development/tutorials/autodoc_ext.html#writing-the-extension.
"""

import warnings

from sphinx.ext.autodoc import AttributeDocumenter, ClassDocumenter
from sphinx.util.inspect import safe_getattr
from traitlets import MetaHasTraits, TraitType, Undefined

# __version__ should be updated using tbump, based on configuration in
# pyproject.toml, according to instructions in RELEASE.md.
#
__version__ = "1.0.0"


class ConfigurableDocumenter(ClassDocumenter):
    """
    Specialized Documenter subclass for traits with config=True

    Links to relevant source code in sphinx.ext.autodoc:
    - Documenter:      https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L270-L299
    - ClassDocumenter: https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L1395-L1408
    """

    # objtype: The suffix to "auto" for a Sphinx directive name that will be
    #          created (and the default value for "directivetype").
    objtype = "configurable"

    # directivetype: Clarifies that this Documenter class could be capable of
    #                documenting this kind of members of other parent like
    #                Documenter classes.
    directivetype = "class"

    # priority: Declares this class' priority for use if multiple classes
    #           "can_document_member" of the "directivetype". This is only
    #           relevant if a parent class has a member.
    #
    #           ConfigurableDocumenter can document traitlets configurable
    #           classes, so a parent like Documenter class can be the
    #           ModuleDocumenter.
    #
    priority = 100  # higher priority than ClassDocumenter's 10

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        """
        If the member is a class with traitlets then we can document it, and we
        will document it thanks to a high priority.

        This function is not considered if the ``autoconfigurable`` or
        ``autoclass`` directives are called directly. can_document_member is
        only used by other parent like Documenter classes having members of this
        class' configured "documentertype" - such as ModuleDocumenter.
        """
        return isinstance(member, MetaHasTraits)

    def get_object_members(self, want_all):
        """
        This get_object_members function override is a hack, manipulating
        __doc__ values of trait configuration objects, but otherwise behaving
        exactly like the super class get_object_members.

        It sets truthy strings to the class' traits __doc__ attributes. They
        will otherwise be filtered out by the Documenter.filter_members
        function, unless ``undoc-members`` option is set.

        Links to relevant source code in sphinx.ext.autodoc:
        - Documenter.filter_members:          https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L616-L769
        - Documenter.get_object_members:      https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L607-L614
        - ClassDocumenter.get_object_members: https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L1656-L1674
        - traitlets.HasTraits.class_traits:   https://github.com/ipython/traitlets/blob/v5.6.0/traitlets/traitlets.py#L1620-L1652
        """
        check, members = super().get_object_members(want_all)

        # We add all _configurable_ traits, including inherited, even if they
        # weren't included via :members: or :inherited-members: options.
        #
        # Being added at this stage doesn't mean they are presented. Any members
        # added here must also have a truthy __doc__ string attribute and not be
        # part of the :exclude-members: option.
        #
        # FIXME: We have been adding the configurable trait_members
        #        unconditionally, but should we keep doing that?
        #
        #        See https://github.com/jupyterhub/autodoc-traits/issues/27
        #
        config_trait_members = self.object.class_traits(config=True).items()
        for trait_tuple in config_trait_members:
            name, trait = trait_tuple
            if not trait.__doc__:
                warnings.warn(
                    f"""
                    Documenting {self.object.__name__}.{trait.name} without a help string because it has config=True.

                    Including undocumented config=True traits is deprecated in autodoc-traits 1.1.
                    Add a help string:

                        {trait.name} = {trait.__class__.__name__}(
                            help="...",
                        )

                    to keep this trait in your docs,
                    or include it explicitly via :members:
                    """,
                    FutureWarning,
                )
                # FIXME: in the unlikely event that the patched trait
                # is documented multiple times in the same build,
                # this patch will cause it to have a truthy help string
                # elsewhere, not just in this autoconfigurable instance.
                trait.__doc__ = trait.help = "No help string is provided."
            if trait_tuple not in members:
                members.append(trait_tuple)

        return check, members


class TraitDocumenter(AttributeDocumenter):
    """
    Links to relevant source code in sphinx.ext.autodoc:
    - Documenter:          https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L270-L299
    - AttributeDocumenter: https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L2509-L2524
    """

    # objtype: The suffix to "auto" for a Sphinx directive name that will be
    #          created (and the default value for "directivetype").
    objtype = "trait"

    # directivetype: Clarifies that this Documenter class could be capable of
    #                documenting this kind of members of other parent like
    #                Documenter classes.
    directivetype = "attribute"

    # priority: Declares this class' priority for use if multiple classes
    #           "can_document_member" of the "directivetype". This is only
    #           relevant if a parent class has a member.
    #
    #           TraitsDocumenter can document traitlets type attributes, so the
    #           parent like Documenter class is typically ClassDocumenter, but
    #           can also be the ConfigurableDocumenter.
    #
    priority = 100  # AttributeDocumenter has 10

    # order: order if the autodoc_member_order in conf.py is set to "groupwise",
    #        by default it is "alphabetical", where lowest order comes first.
    #        Since traits are relevant configuration, we declare the lowest
    #        order for high visual priority.
    member_order = 0  # AttributeDocumenter has 60

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        """
        If the member is a traitlets type we can document it, and we will
        document it thanks to a high priority.

        This function is not considered if the ``autotrait`` or
        ``autoattribute`` directives are called directly. can_document_member is
        only used by other parent like Documenter classes having members of this
        class' configured "documentertype" - such as ClassDocumenter.
        """
        return isinstance(member, TraitType)

    def add_directive_header(self, sig):
        """
        add_directive_header is called by the base class' Documenter.generate
        method. It is provided by both AttributeDocumenter and Documenter. This
        override retains use of the super classes implementations, but influence
        them.

        For functions, the directive header describes the function's call
        signature, but not the function's docstring.

        Similarly, we look to emit rST to describe how the traitlets
        configuration option can be configured and its default value.

        - Documenter.generate:                      https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L918-L929
        - AttributeDocumenter.add_directive_header: https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L2592-L2620
        - Documenter.add_directive_header:          https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L504-L524
        """
        default_value = self.object.default_value
        if default_value is Undefined:
            default_value = ""
        else:
            default_value = repr(default_value)

        traitlets_type = self.object.__class__.__name__  # Bool

        if self.object.metadata.get("config"):
            # add config prefix (c.TestConfigurator.trait = ) if it's configurable
            config_prefix = f"c.{self.format_name()} = "
        else:
            config_prefix = ""

        self.options.annotation = f"{config_prefix}{traitlets_type}({default_value})"

        super().add_directive_header(sig)


def hastraits_attrgetter(obj, name, *defargs):
    """getattr for trait

    Ensures when HasTraits are documented, their __doc__ attr is defined
    as the .help string.

    This backports a change in traitlets 5.8.0.
    """
    attr = safe_getattr(obj, name, *defargs)
    if isinstance(attr, TraitType):
        # ensure __doc__ is defined as the trait's help string
        # if help is empty, that's the same as undocumented
        attr.__doc__ = attr.help
    return attr


def setup(app):
    """
    The setup function is required for Sphinx extensions.

    In this function we register the sphinx.ext.autodoc extension that this
    extension needs to function, and we register our sphinx.ext.autodoc
    Documenter classes we provide.
    """
    # setup_extension reference:
    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.setup_extension
    app.setup_extension("sphinx.ext.autodoc")

    # add_autodocumenter reference:
    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_autodocumenter
    app.add_autodocumenter(ConfigurableDocumenter)
    app.add_autodocumenter(TraitDocumenter)

    # add_autodoc_attrgetter reference:
    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_autodoc_attrgetter
    app.add_autodoc_attrgetter(MetaHasTraits, hastraits_attrgetter)
