import os
import sys
from typing import List

INIT_FILE_NAME = "__init__.py"
PYCACHE_FOLDER_NAME = "__pycache__"
PYTHON_EXTENSION = ".py"


def add_missing_init_files_from_path(paths: List[str]) -> None:
    for path in paths:
        root_directory = path if os.path.isdir(path) else os.path.dirname(path)
        add_missing_init_files(root_directory)


def add_missing_init_files(root_directory: str) -> None:
    """
    Add missing __init__.py files to the specified root directory and subdirectories that contain at least one python
    module (the python module does not have to be in the directory directly, it can be in a subdirectory.

    Parameters
    ----------
    root_directory
        Root path containing the python code.
    Returns
    -------
    None
    """
    for dirpath, _, filenames in os.walk(root_directory):
        if INIT_FILE_NAME not in filenames and directory_contains_python(
            dirpath,
        ):
            print(f"Adding {INIT_FILE_NAME} in {dirpath}")
            open(os.path.join(dirpath, INIT_FILE_NAME), "a").close()


def directory_contains_python(root_directory: str) -> bool:
    """
    Return true if the specified folder or one of its subfolders contain a python file (with .py extension), false otherwise.

    Parameters
    ----------
    root_directory
        Root directory to scan

    Returns
    -------
    A bool indicating if the specified folder contain a python file.
    """
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if any(
            PYTHON_EXTENSION == os.path.splitext(extension)[-1]
            for extension in filenames
        ):
            return True
        for dirname in dirnames:
            if dirname == PYCACHE_FOLDER_NAME:
                continue
            if directory_contains_python(os.path.join(dirpath, dirname)):
                return True
    return False
