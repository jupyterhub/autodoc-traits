autoconfigurable - specified members
====================================

The ``members`` option with specified members should only present the specified
members.

In this test we list the member ``method`` and ``trait_nohelp``. One may expect
no members besides these to show up, but we present them and all trait members
still, see `Issue27`_.

.. _Issue27: https://github.com/jupyterhub/autodoc-traits/issues/27

.. autoconfigurable:: test_module.TestConfigurable
   :noindex:
   :members: method,trait_nohelp
