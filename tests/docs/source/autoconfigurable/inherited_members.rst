autoconfigurable - inherited-members
====================================

With the ``inherited-members`` option, we expect traits from the superclass
SampleConfigurable to show up as well as traits from SampleConfigurableSubclass.

.. note::
   Several members from the ``traitlets.HasTraits`` base class are excluded for
   now as they cause the sphinx-build warning of ``Unexpected section title`` in
   sphinx 4.

.. autoconfigurable:: sample_module.SampleConfigurableSubclass
   :noindex:
   :inherited-members:
   :exclude-members: class_config_section,observe,on_trait_change,trait_defaults,trait_events,trait_values,unobserve
