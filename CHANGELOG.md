# Changes in autodoc-traits

## 1.0

### 1.1.0 - 2022-12-20

([full changelog](https://github.com/jupyterhub/autodoc-traits/compare/1.0.0...1.1.0))

#### Enhancements made

- Automatically register the sphinx.ext.autodoc extension [#18](https://github.com/jupyterhub/autodoc-traits/pull/18) ([@consideRatio](https://github.com/consideRatio))

#### Bugs fixed

- register traits with a help string as documented for `autoclass` [#33](https://github.com/jupyterhub/autodoc-traits/pull/33) ([@minrk](https://github.com/minrk))
- avoid putting `c.Class.trait` annotation on non-config traits [#32](https://github.com/jupyterhub/autodoc-traits/pull/32) ([@minrk](https://github.com/minrk))
- Add tests, add docstrings, and fix small bugs [#28](https://github.com/jupyterhub/autodoc-traits/pull/28) ([@consideRatio](https://github.com/consideRatio))

#### Maintenance and upkeep improvements

- Add tests, add docstrings, and fix small bugs [#28](https://github.com/jupyterhub/autodoc-traits/pull/28) ([@consideRatio](https://github.com/consideRatio))
- single file module [#25](https://github.com/jupyterhub/autodoc-traits/pull/25) ([@minrk](https://github.com/minrk))
- maint: refactor `__init__.py` and add _version.py, drop setup.py, require python 3.7+ [#21](https://github.com/jupyterhub/autodoc-traits/pull/21) ([@consideRatio](https://github.com/consideRatio))

#### Documentation improvements

- Add tests, add docstrings, and fix small bugs [#28](https://github.com/jupyterhub/autodoc-traits/pull/28) ([@consideRatio](https://github.com/consideRatio))
- docs: add fixme note about unexpected inherited-members option [#16](https://github.com/jupyterhub/autodoc-traits/pull/16) ([@consideRatio](https://github.com/consideRatio))

#### Continuous integration improvements

- Bump pypa/gh-action-pypi-publish from 1.4.1 to 1.6.4 [#23](https://github.com/jupyterhub/autodoc-traits/pull/23) ([@dependabot](https://github.com/dependabot))
- ci: add dependabot.yaml and update release workflow [#20](https://github.com/jupyterhub/autodoc-traits/pull/20) ([@consideRatio](https://github.com/consideRatio))

#### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterhub/autodoc-traits/graphs/contributors?from=2022-12-06&to=2022-12-20&type=c))

[@consideRatio](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3AconsideRatio+updated%3A2022-12-06..2022-12-20&type=Issues) | [@minrk](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Aminrk+updated%3A2022-12-06..2022-12-20&type=Issues)

### 1.0.0 - 2022-12-06

Let's call it 1.0!

([full changelog](https://github.com/jupyterhub/autodoc-traits/compare/0.1.0...1.0.0))

#### Bugs fixed

- Fix failure to use autoclass on non-traitlets configurable classes [#10](https://github.com/jupyterhub/autodoc-traits/pull/10) ([@blink1073](https://github.com/blink1073), [@consideRatio](https://github.com/consideRatio))

#### Maintenance and upkeep improvements

- pre-commit: add typical jupyterhub org config [#15](https://github.com/jupyterhub/autodoc-traits/pull/15) ([@consideRatio](https://github.com/consideRatio), [@minrk](https://github.com/minrk))

#### Documentation improvements

- Refresh README, RELEASE, and CHANGELOG [#14](https://github.com/jupyterhub/autodoc-traits/pull/14) ([@consideRatio](https://github.com/consideRatio), [@minrk](https://github.com/minrk))
- Point url to the GitHub repo [#8](https://github.com/jupyterhub/autodoc-traits/pull/8) ([@yuvipanda](https://github.com/yuvipanda), [@consideRatio](https://github.com/consideRatio))
- add changelog.md, release.md, README badges [#7](https://github.com/jupyterhub/autodoc-traits/pull/7) ([@minrk](https://github.com/minrk), [@yuvipanda](https://github.com/yuvipanda), [@consideRatio](https://github.com/consideRatio))

#### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterhub/autodoc-traits/graphs/contributors?from=2021-10-22&to=2022-12-06&type=c))

[@blink1073](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Ablink1073+updated%3A2021-10-22..2022-12-06&type=Issues) | [@consideRatio](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3AconsideRatio+updated%3A2021-10-22..2022-12-06&type=Issues) | [@minrk](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Aminrk+updated%3A2021-10-22..2022-12-06&type=Issues) | [@willingc](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Awillingc+updated%3A2021-10-22..2022-12-06&type=Issues) | [@yuvipanda](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Ayuvipanda+updated%3A2021-10-22..2022-12-06&type=Issues)

## 0.1

### 0.1.0 - 2021-10-22

0.1.0 is the first stable release of autodoc-traits.
It fixes compatibility with sphinx 4 from the previously published 0.1.0dev prerelease.

#### Merged PRs

- add publish github action [#4](https://github.com/jupyterhub/autodoc-traits/pull/4) ([@minrk](https://github.com/minrk))
- Remove unused import of deprecated PyClassmember [#3](https://github.com/jupyterhub/autodoc-traits/pull/3) ([@minrk](https://github.com/minrk))
- Remove duplicates in documenting trait members [#1](https://github.com/jupyterhub/autodoc-traits/pull/1) ([@rkdarst](https://github.com/rkdarst))

#### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterhub/autodoc-traits/graphs/contributors?from=2019-09-06&to=2021-10-22&type=c))

[@betatim](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Abetatim+updated%3A2019-09-06..2021-10-22&type=Issues) | [@minrk](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Aminrk+updated%3A2019-09-06..2021-10-22&type=Issues) | [@rkdarst](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Arkdarst+updated%3A2019-09-06..2021-10-22&type=Issues) | [@welcome](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Awelcome+updated%3A2019-09-06..2021-10-22&type=Issues) | [@willingc](https://github.com/search?q=repo%3Ajupyterhub%2Fautodoc-traits+involves%3Awillingc+updated%3A2019-09-06..2021-10-22&type=Issues)
