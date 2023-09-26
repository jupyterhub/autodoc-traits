"""
sample_module docstring

This module provides a module and classes with and without traits to test
autodoc_traits against. It does not contain tests.
"""

from traitlets import Bool, Dict, Instance, Integer, Unicode, Union
from traitlets.config.configurable import Configurable


class SampleConfigurable(Configurable):
    """SampleConfigurable docstring"""

    non_trait = False

    @property
    def non_trait_property(self):
        """non_trait_property docstring"""

    trait = Bool(
        help="""trait help text""",
        config=True,
    )
    trait_nohelp = Bool(
        config=True,
    )
    trait_noconfig = Bool(
        help="""trait_noconfig help text""",
    )

    def method(self):
        """method docstring"""


class SampleConfigurableSubclass(SampleConfigurable):
    """SampleConfigurableSubclass docstring"""

    subclass_non_trait = False

    @property
    def subclass_non_trait_property(self):
        """subclass_non_trait_property docstring"""

    subclass_trait = Bool(
        config=True,
        help="""subclass_trait help text""",
    )
    subclass_trait_nohelp = Bool(
        config=True,
    )
    subclass_trait_noconfig = Bool(
        help="""subclass_trait_noconfig help text""",
    )

    def subclass_method(self):
        """subclass_method docstring"""


class SampleNonConfigurable:
    """SampleNonConfigurable docstring"""

    non_trait = False

    @property
    def non_trait_property(self):
        """non_trait_property docstring"""

    def method(self):
        """method docstring"""


class SampleNonConfigurableSubclass(SampleNonConfigurable):
    """SampleNonConfigurableSubclass docstring"""

    non_trait = False

    @property
    def subclass_non_trait_property(self):
        """subclass_non_trait_property docstring"""

    def subclass_method(self):
        """subclass_method docstring"""


class TraitTypesSampleConfigurable(Configurable):
    """TraitTypesSampleConfigurable docstring"""

    trait_integer = Integer(
        help="""trait_integer help text""",
        config=True,
    )
    trait_integer_nohelp = Integer(
        config=True,
    )
    trait_integer_noconfig = Integer(
        help="""trait_integer_noconfig help text""",
    )

    trait_unicode = Unicode(
        help="""trait_unicode help text""",
        config=True,
    )
    trait_unicode_nohelp = Unicode(
        config=True,
    )
    trait_unicode_noconfig = Unicode(
        help="""trait_unicode_noconfig help text""",
    )

    trait_dict = Dict(
        help="""trait_dict help text""",
        config=True,
    )
    trait_dict_nohelp = Dict(
        config=True,
    )
    trait_dict_noconfig = Dict(
        help="""trait_dict_noconfig help text""",
    )

    trait_instance = Instance(
        klass=SampleConfigurable,
        help="""trait_instance help text""",
        config=True,
    )
    trait_instance_nohelp = Instance(
        klass=SampleConfigurable,
        config=True,
    )
    trait_instance_noconfig = Instance(
        klass=SampleConfigurable,
        help="""trait_instance_noconfig help text""",
    )

    trait_union = Union(
        [Integer(), Unicode()],
        help="""trait_union help text""",
        config=True,
    )
    trait_union_nohelp = Union(
        [Integer(), Unicode()],
        config=True,
    )
    trait_union_noconfig = Union(
        [Integer(), Unicode()],
        help="""trait_union_noconfig help text""",
    )
