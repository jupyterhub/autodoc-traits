# How to make a release

`autodoc-traits` is a package [available on
PyPI][pypi].
These are instructions on how to make a release on PyPI.
The PyPI release is done automatically by GitHub Actions when a tag is pushed.

To follow these instructions, you need:

- To have push rights to the [autodoc-traits GitHub
  repository][repo].

[pypi]: https://pypi.org/project/autodoc-traits
[repo]: https://github.com/jupyterhub/autodoc-traits

## Steps to make a release

1. Checkout main and make sure it is up to date.

   ```shell
   ORIGIN=${ORIGIN:-origin} # set to the canonical remote, e.g. 'upstream' if 'origin' is not the official repo
   git checkout main
   git fetch $ORIGIN main
   ```

1. Update [CHANGELOG.md](CHANGELOG.md). Doing this can be made easier with the
   help of the
   [choldgraf/github-activity](https://github.com/choldgraf/github-activity)
   utility.

1. Set the `__version__` variable in [\_\_init.py\_\_][]
   appropriately and make a commit.

   ```
   git add autodoc_traits/__init__.py
   VERSION=...  # e.g. 1.2.3
   git commit -m "release $VERSION"
   ```

[\_\_init.py\_\_]: autodoc_traits/__init__.py

1. Reset the `__version__` variable in
   [\_\_init.py\_\_][] appropriately with an incremented
   patch version and `.dev` suffix, then make a commit.

   ```
   git add autodoc_traits/__init__.py
   git commit -m "back to dev"
   ```

1. Push your two commits to main.

   ```bash
   # first push commits without a tags to ensure the
   # commits comes through, because a tag can otherwise
   # be pushed all alone without company of rejected
   # commits, and we want have our tagged release coupled
   # with a specific commit
   git push $ORIGIN main
   ```

1. Create a git tag for the pushed release commit and push it.

   ```shell
   git tag -a $VERSION -m $VERSION HEAD~1
   # verify you tagged the right commit
   git log

   # then push it
   git push $ORIGIN $VERSION
   ```
