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
   git pull $ORIGIN main
   ```

1. Update [CHANGELOG.md](CHANGELOG.md). Doing this can be made easier with the
   help of the
   [choldgraf/github-activity](https://github.com/choldgraf/github-activity)
   utility.

1. Publish the new version with [tbump][]

   ```
   tbump 1.2.3
   ```

1. Reset the version to next.dev (e.g. 1.2.3 -> 1.3.0.dev)

   ```
   tbump --no-tag 1.3.0.dev
   ```

[tbump]: https://github.com/dmerejkowsky/tbump
