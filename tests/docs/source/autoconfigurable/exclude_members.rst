autoconfigurable - exclude-members
==================================

The ``exclude-members`` option should work to exclude specific members, trait
members and and non-traits members alike.

In this test we provide ``members`` and then exclude the members ``trait``
and ``method`` by specifying them with ``exclude-members`` that otherwise ought
to show up, and check that they aren't showing up.

.. autoconfigurable:: sample_module.SampleConfigurable
   :noindex:
   :members:
   :exclude-members: trait,method
