__version__ = "1.0.0.dev"


def setup(app, *args, **kwargs):
    from .autodoc_traits import setup

    return setup(app, *args, **kwargs)
