import setuptools

from autodoc_traits import __version__ as version

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autodoc-traits",
    version=version,
    author="Jupyter Development Team",
    author_email="jupyter@googlegroups.com",
    description="Sphinx extension to autodoc traitlets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jupyterhub/autodoc-traits",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["sphinx", "traitlets"],
)
