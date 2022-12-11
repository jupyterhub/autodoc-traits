# About the test suite

We use `pytest` to run `sphinx-build` against the Sphinx project in the `docs/`
folder. Besides concluding that the build succeeds without warnings, we look for
strings in the .html files to estimate if it has rendered as it should or not.

The test .rst documents include some descriptions about whats tested.

## Inspecting the test documentation

`sphinx-autobuild` is convenient to use when looking to inspect or expand the
content in the docs/ folder, which rendered is whats inspected by the test
suite.

```shell
pip install sphinx-autobuild

cd docs
# --watch:     we watch python files influencing the built documentation
# --pre-build: we rebuild from scratch as changes to the python files
#              can influence all built html
sphinx-autobuild \
    --open-browser \
    --watch="test_module.py" \
    --watch="../../autodoc_traits.py" \
    --pre-build="rm -rf build" \
    --ignore
    source \
    build
```
