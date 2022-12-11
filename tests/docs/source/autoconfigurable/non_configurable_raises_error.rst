autoconfigurable - non configurable class
=========================================

Test that we error when used on non-configurable classes.

.. note::
   This file is targeted by ``exclude_patterns`` in ``source/conf.py``
   to avoid failing unless we want to explicitly test such failure.

.. autoconfigurable:: test_module.TestNonConfigurable
   :noindex:
