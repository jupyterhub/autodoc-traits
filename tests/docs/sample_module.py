"""
sample_module docstring

This module provides a module and classes with and without traits to test
autodoc_traits against. It does not contain tests.
"""

from traitlets import Bool
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
