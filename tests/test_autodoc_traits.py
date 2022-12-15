import os
import subprocess

import pytest


def test_sphinx_build_all_docs(temp_docs_dir, monkeypatch):
    """
    Tests that the docs folder builds without warnings.
    """
    monkeypatch.chdir(temp_docs_dir)

    subprocess.run(
        ["sphinx-build", "--color", "-W", "--keep-going", "source", "build"],
        check=True,
        text=True,
    )


@pytest.mark.parametrize(
    "rst_file_to_test, strings_in_html, strings_not_in_html",
    [
        (
            "autoclass/members.rst",
            [],
            [
                "c.SampleConfigurable.trait",
            ],
        ),
        (
            "autoclass/undoc_members.rst",
            [
                "c.SampleConfigurable.trait",
            ],
            [],
        ),
        (
            "autoconfigurable/exclude_members.rst",
            ["c.SampleConfigurable.trait_nohelp"],
            [
                "trait help text",
                "method docstring",
            ],
        ),
        (
            "autoconfigurable/inherited_members.rst",
            [
                "c.SampleConfigurableSubclass.trait",
                "c.SampleConfigurableSubclass.subclass_trait",
                "method docstring",
            ],
            [],
        ),
        (
            "autoconfigurable/members.rst",
            [
                "c.SampleConfigurableSubclass.subclass_trait",
                "c.SampleConfigurableSubclass.trait",
                "method docstring",
            ],
            [
                "trait_noconfig help text",
            ],
        ),
        (
            "autoconfigurable/no_members.rst",
            [
                "c.SampleConfigurableSubclass.subclass_trait",
                "c.SampleConfigurableSubclass.trait",
            ],
            [
                "trait_noconfig help text",
                "method docstring",
            ],
        ),
        ("autoconfigurable/non_configurable_raises_error.rst", [], []),
        (
            "autoconfigurable/specified_members.rst",
            [
                "method docstring",
                "c.SampleConfigurable.trait_nohelp",
                "trait help text",
            ],
            [],
        ),
        (
            "automodule/members.rst",
            [
                "sample_module docstring",
                "SampleConfigurable docstring",
                "SampleConfigurableSubclass docstring",
                "SampleNonConfigurable docstring",
                "SampleNonConfigurableSubclass docstring",
            ],
            [],
        ),
        (
            "autotrait/help.rst",
            [
                "c.SampleConfigurable.trait",
                "trait help text",
            ],
            [],
        ),
        (
            "autotrait/noconfig.rst",
            [
                "Bool(False)",
            ],
            [
                "c.SampleConfigurable.trait_noconfig",
            ],
        ),
        (
            "autotrait/nohelp.rst",
            [
                "c.SampleConfigurable.trait_nohelp",
            ],
            [],
        ),
        ("autotrait/non_trait_raises_error.rst", [], []),
    ],
)
def test_sphinx_build_file(
    get_glob_filtered_temp_docs_dir,
    monkeypatch,
    rst_file_to_test,
    strings_in_html,
    strings_not_in_html,
):
    """
    Tests that individual .rst documents in the docs folder builds without
    warnings, emits .html with certain strings, and emits .html without certain
    strings.
    """
    temp_docs_dir = get_glob_filtered_temp_docs_dir(["index.rst", rst_file_to_test])
    monkeypatch.chdir(temp_docs_dir)

    p = subprocess.run(
        [
            "sphinx-build",
            "--color",
            "-W",
            "--keep-going",
            "-D",
            "exclude_patterns=",
            "source",
            "build",
        ],
        text=True,
    )
    if "raises_error" in rst_file_to_test:
        assert p.returncode > 0
        return
    assert p.returncode == 0

    html_file_to_inspect = os.path.join(
        "build", rst_file_to_test.replace(".rst", ".html")
    )
    with open(html_file_to_inspect) as f:
        html = f.read()

    for s in strings_in_html:
        assert s in html

    for s in strings_not_in_html:
        assert s not in html
