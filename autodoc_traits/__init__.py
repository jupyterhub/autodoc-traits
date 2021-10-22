__version__ = "0.1.0"


def setup(app, *args, **kwargs):
    from .autodoc_traits import setup

    return setup(app, *args, **kwargs)
