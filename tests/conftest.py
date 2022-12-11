import glob
import os
import shutil
import sys
import tempfile
from functools import partial

import pytest

if sys.version_info >= (3, 8):
    copy_tree = partial(shutil.copytree, dirs_exist_ok=True)
else:
    # use deprecated distutils on Python < 3.8
    # when shutil.copytree added dirs_exist_ok support
    from distutils.dir_util import copy_tree


@pytest.fixture
def temp_docs_dir():
    """
    This fixture provides a temporary directory with files copied from the
    tests/docs directory.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        tests_dir = os.path.abspath(os.path.dirname(__file__))
        test_docs_dir = os.path.join(tests_dir, "docs")

        # populate content
        copy_tree(test_docs_dir, temp_dir)

        yield temp_dir


@pytest.fixture
def get_glob_filtered_temp_docs_dir(temp_docs_dir):
    """
    This fixture provides function that returns a path to a temp docs directory
    based on tests/docs, but filtered to only retain .rst files globbed by
    provide glob_patterns relative to the source/ directory.

    Note that to test specific documents, including those that are expected to
    raise errors, we could use the Sphinx configuration "include_patterns".
    Sadly its only available in Sphinx 5.1+ so it would constrain us to test
    against Sphinx 5.1+. Due to that, we rely on this fixture instead.
    """

    def _filter_source_dir_func(glob_patterns):
        old_cwd = os.getcwd()
        try:
            os.chdir(os.path.join(temp_docs_dir, "source"))
            source_rst_files = set(glob.glob("**/*.rst", recursive=True))
            files_to_retain = set()
            for p in glob_patterns:
                files_to_retain = files_to_retain.union(
                    set(glob.glob(p, recursive=True))
                )

            if not source_rst_files.intersection(files_to_retain):
                print("glob_patterns", glob_patterns)
                print("source_rst_files", source_rst_files)
                print("files_to_retain", files_to_retain)
                raise ValueError(
                    "provided glob_patterns found no .rst in the source folder to retain!"
                )

            for f in source_rst_files.difference(files_to_retain):
                os.remove(f)

            print()
            print(
                f"Fixture get_glob_filtered_temp_docs_dir provided the directory {temp_docs_dir}:"
            )
            for f in glob.glob("**/*.rst", recursive=True):
                print(f"- {f}")
            print()
        finally:
            os.chdir(old_cwd)
        return temp_docs_dir

    yield _filter_source_dir_func
