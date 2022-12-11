import os


def test_temp_docs_dir(temp_docs_dir):
    """
    Verify that we get a reference to a temporary directory with source/conf.py
    in it.
    """
    assert os.path.isdir(os.path.join(temp_docs_dir, "source"))
    assert os.path.isfile(os.path.join(temp_docs_dir, "source/conf.py"))


def test_get_glob_filtered_temp_docs_dir(get_glob_filtered_temp_docs_dir):
    """
    Verify that we get a reference to a temporary directory with:
    - source/conf.py
    - index.rst files retained
    - filtered .rst files removed
    - non-filtered .rst files retained
    """
    temp_docs_dir = get_glob_filtered_temp_docs_dir(
        ["index.rst", "automodule/members.rst"]
    )
    assert os.path.isdir(os.path.join(temp_docs_dir, "source"))
    assert os.path.isfile(os.path.join(temp_docs_dir, "source/conf.py"))
    assert os.path.isfile(os.path.join(temp_docs_dir, "source/index.rst"))
    assert os.path.isfile(os.path.join(temp_docs_dir, "source/automodule/members.rst"))
    assert not os.path.isfile(
        os.path.join(temp_docs_dir, "source/autoclass/members.rst")
    )
