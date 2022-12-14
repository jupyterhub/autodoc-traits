autoconfigurable - members
==========================

The ``members`` option without specified members should present all class
members.

In this test expect all trait members with ``.config(True)`` to show up, even
those inherited from super classes.

.. autoconfigurable:: sample_module.SampleConfigurableSubclass
   :noindex:
   :members:
