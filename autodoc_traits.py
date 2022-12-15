"""
sphinx.ext.autodoc extension for classes with configurable traits.

The code here is similar to the official code example in
https://www.sphinx-doc.org/en/master/development/tutorials/autodoc_ext.html#writing-the-extension.
"""
from sphinx.ext.autodoc import AttributeDocumenter, ClassDocumenter
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

        truthy_string = (
            "A hack is used by autodoc_traits since 1.1.0 for trait "
            "configurations, updating trait configuration's __doc__ to this "
            "truthy string as required to make sphinx.ext.autodoc behave as "
            " wanted."
        )
        for trait in self.object.class_traits(config=True).values():
            trait.__doc__ = truthy_string

        # We add all traits, also the inherited, bypassing :members: and
        # :inherit-members: options.
        #
        # FIXME: We have been adding the trait_members unconditionally, but
        #        should we keep doing that?
        #
        #        See https://github.com/jupyterhub/autodoc-traits/issues/27
        #
        trait_members = self.object.class_traits(config=True).items()
        for trait in trait_members:
            if trait not in members:
                members.append(trait)

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
        default_value = self.object.get_default_value()
        if default_value is Undefined:
            default_value = ""
        else:
            default_value = repr(default_value)

        self.options.annotation = "c.{name} = {traitlets_type}({default_value})".format(
            name=self.format_name(),  # TestConfigurator.trait
            traitlets_type=self.object.__class__.__name__,  # Bool
            default_value=default_value,
        )

        super().add_directive_header(sig)

    def get_doc(self):
        """
        get_doc (get docstring) is called by add_content, which is called by
        generate. We override it to not unconditionally provide the docstring of
        the traitlets type, but instead provide the traits help text if its
        available.

        Links to relevant source code in sphinx.ext.autodoc:
        - Documenter.generate:             https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L918-L929
        - AttributeDocumenter.add_content: https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L2655-L2663
        - Documenter.add_content:          https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L568-L605
        - AttributeDocumenter.get_doc:     https://github.com/sphinx-doc/sphinx/blob/v6.0.0b2/sphinx/ext/autodoc/__init__.py#L2639-L2653
        """
        if isinstance(self.object.help, str):
            return [[self.object.help]]
        return super().get_doc()


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
