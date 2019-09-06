# autodoc-traits

Sphinx extension to autodocument configuration files using the [traitlets](https://github.com/ipython/traitlets) library

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
