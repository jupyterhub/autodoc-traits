# autodoc-traits

[![Latest PyPI version](https://img.shields.io/pypi/v/autodoc-traits?logo=pypi)](https://pypi.python.org/pypi/autodoc-traits)
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jupyterhub/autodoc-traits/issues)
[![Discourse](https://img.shields.io/badge/help_forum-discourse-blue?logo=discourse)](https://discourse.jupyter.org/c/jupyterhub)
[![Gitter](https://img.shields.io/badge/social_chat-gitter-blue?logo=gitter)](https://gitter.im/jupyterhub/jupyterhub)

Sphinx extension to autodocument configuration files using the [traitlets](https://github.com/ipython/traitlets) library.

## Install

```bash
python3 -m pip install autodoc-traits
```

## Usage

Add `autodoc_traits` to the `extensions` list in
a Sphinx `conf.py` file:

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'autodoc_traits',
    'sphinx_copybutton',
]
```
