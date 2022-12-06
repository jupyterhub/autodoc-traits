"""
sphinx.ext.autodoc extension for classes with configurable traits.

The code here is similar to the official code example in
https://www.sphinx-doc.org/en/master/development/tutorials/autodoc_ext.html#writing-the-extension.
"""
from sphinx.ext.autodoc import AttributeDocumenter, ClassDocumenter
from traitlets import MetaHasTraits, TraitType, Undefined


class ConfigurableDocumenter(ClassDocumenter):
    """Specialized Documenter subclass for traits with config=True"""

    objtype = "configurable"
    directivetype = "class"

    def get_object_members(self, want_all):
        """Add traits with .tag(config=True) to members list"""
        check, members = super().get_object_members(want_all)
        if not isinstance(self.object, MetaHasTraits):
            return check, members
        get_traits = (
            self.object.class_own_traits
            if self.options.inherited_members
            else self.object.class_traits
        )
        trait_members = []
        for name, trait in sorted(get_traits(config=True).items()):
            # put help in __doc__ where autodoc will look for it
            trait.__doc__ = trait.help
            trait_members.append((name, trait))
        # Remove duplicates between members and trait_members.  We
        # can't use sets, because not all items are hashable.  Modify
        # trait_members in place for returning.
        for item in members:
            if item not in trait_members:
                trait_members.append(item)
        return check, trait_members


class TraitDocumenter(AttributeDocumenter):
    objtype = "trait"
    directivetype = "attribute"
    member_order = 1
    priority = 100

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, TraitType)

    def add_directive_header(self, sig):
        default = self.object.get_default_value()
        if default is Undefined:
            default_s = ""
        else:
            default_s = repr(default)
        self.options.annotation = "c.{name} = {trait}({default})".format(
            name=self.format_name(),
            trait=self.object.__class__.__name__,
            default=default_s,
        )
        super().add_directive_header(sig)


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
