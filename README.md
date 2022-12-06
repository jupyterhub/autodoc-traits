# autodoc-traits

[![Latest PyPI version](https://img.shields.io/pypi/v/autodoc-traits?logo=pypi)](https://pypi.python.org/pypi/autodoc-traits)
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jupyterhub/autodoc-traits/issues)
[![Discourse](https://img.shields.io/badge/help_forum-discourse-blue?logo=discourse)](https://discourse.jupyter.org/c/jupyterhub)
[![Gitter](https://img.shields.io/badge/social_chat-gitter-blue?logo=gitter)](https://gitter.im/jupyterhub/jupyterhub)

`autodoc-traits` is a Sphinx extension that influences
[`sphinx.ext.autodoc`][]'s provided [Sphinx directives][], specifically
[`autoclass`][] and [`autoattribute`][], to better document classes with
[Traitlets][] based configuration.

The `autoclass` directive is updated to document class attributes inheriting
from [`traitlets.TraitType`][] by default. The `autoattribute` directive is
updated to provide a header looking like `default_url c.KubeSpawner.default_url
= Unicode('')`.

The extension also provides the `autoconfigurable` directive mapping to the
`autoclass` directive, and the `autotrait` directive mapping to the
`autoattributes` directive.

## How to use it

1. Install `autodoc-traits`:

   ```shell
   pip install autodoc-traits
   ```

2. Configure Sphinx to use the `autodoc_traits` and `sphinx.ext.autodoc`
   extensions in a Sphinx projects `conf.py` file:

   ```python
   # -- General Sphinx configuration --------------------------------------------
   # ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
   #
   extensions = [
       "autodoc_traits",
       "sphinx.ext.autodoc",
       # ...
   ]
   ```

3. Make use of a `sphinx.ext.autodoc` Sphinx directive like `autoclass`, or
   `automodule` that make use of `autoclass`:


   From a .rst document:

   ```rst
   .. autoclass:: KubeSpawner
   ```

## Use with MyST Parser

   While you can use [`myst-parser`][], `sphinx.ext.autodoc`'s directives emits
   unparsed rST, forcing us to parse the autodoc directives in a rST context.

   From a .md document, with `myst-parser`:

   ````markdown
   ```{eval-rst}
   .. autoclass:: KubeSpawner
   ```
   ````

  Due to this, also the Python docstrings are required to be in rST as well.
  Addressing this can be tracked from [executablebooks/team-compass issue
  #6](https://github.com/executablebooks/team-compass/issues/6).

[`sphinx.ext.autodoc`]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[sphinx directives]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives
[`autoclass`]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoclass
[`autoattribute`]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoattribute
[traitlets]: https://github.com/ipython/traitlets
[`traitlets.TraitType`]: https://traitlets.readthedocs.io/en/stable/trait_types.html#traitlets.TraitType
[`myst-parser`]: https://myst-parser.readthedocs.io/en/latest/
