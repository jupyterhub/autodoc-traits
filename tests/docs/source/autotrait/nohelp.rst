autotrait - no help
===================

Test that we fall back to present the trait's header even if it lacks a ``help``
string.

.. note::

   This may include the missing help string message
   if built together with autoconfigurable,
   which patches config=True traits to have a truthy help string.
   This is unrealistic in real docs, but also fairly harmless.

.. autotrait:: sample_module.SampleConfigurable.trait_nohelp
   :noindex:
