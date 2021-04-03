import argparse
import os
from typing import List

INIT_FILE_NAME = "__init__.py"


def add_missing_init_files_from_path(
    paths: List[str],
    folders_to_ignore: List[str],
    source_extensions: List[str],
    folder_trees_to_ignore: List[str],
) -> None:
    """
    Add missing __init__.py files to the specified root directories and subdirectories that contain at least one python
    module (the python module does not have to be in the directory directly, it can be in a subdirectory.

    Parameters
    ----------
    paths
        List of root path containing the python code.
    folders_to_ignore
        List of folders paths that will be excluded. The folder path should be relative to the source_tree. Their subdirectories will NOT be excluded.
    source_extensions
         Files with these extensions will be considered python source code.
    folder_trees_to_ignore
        List of folders names that will be excluded. Their subdirectories will ALSO be excluded.

    Returns
    -------
    None
    """
    if isinstance(paths, str):
        paths = [paths]

    for path in paths:
        if not os.path.exists(path):
            exit(f"Cannot find path {path}")
        root_directory = path if os.path.isdir(path) else os.path.dirname(path)
        add_missing_init_files(
            root_directory,
            folders_to_ignore,
            source_extensions,
            folder_trees_to_ignore,
        )


def add_missing_init_files(
    root_directory: str,
    folders_to_ignore: List[str],
    source_extensions: List[str],
    folder_trees_to_ignore: List[str],
) -> None:
    """
    Add missing __init__.py files to the specified root directory and subdirectories that contain at least one python
    module (the python module does not have to be in the directory directly, it can be in a subdirectory.

    Parameters
    ----------
    root_directory
        Root path containing the python code.
    folders_to_ignore
        List of folders paths that will be excluded. The folder path should be relative to the source_tree. Their subdirectories will NOT be excluded.
    source_extensions
         Files with these extensions will be considered python source code.
    folder_trees_to_ignore
         List of folders names that will be excluded. Their subdirectories will ALSO be excluded.

    Returns
    -------
    None
    """
    if not os.path.exists(root_directory):
        exit(f"Cannot find directory {root_directory}")
    if not os.path.isdir(root_directory):
        exit(f"{root_directory} is not a directory")

    for dirpath, _, filenames in os.walk(root_directory):
        if dirpath in folders_to_ignore:
            continue
        if INIT_FILE_NAME not in filenames and directory_contains_python(
            dirpath,
            source_extensions,
            folder_trees_to_ignore,
        ):
            print(f"Adding {INIT_FILE_NAME} in {dirpath}")
            open(os.path.join(dirpath, INIT_FILE_NAME), "a").close()


def directory_contains_python(
    root_directory: str,
    extensions: List[str],
    folder_trees_to_ignore: List[str],
) -> bool:
    """
    Return true if the specified folder or one of its subfolders contain a python file (with .py extension), false otherwise.

    Parameters
    ----------
    root_directory
        Root directory to scan
    extensions
        Files with these extensions will be considered python source code.
    folder_trees_to_ignore
        List of folders names that will be excluded. Their subdirectories will ALSO be excluded.

    Returns
    -------
    A bool indicating if the specified folder contain a python file.
    """
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if any(
            os.path.splitext(extension)[-1] in extensions for extension in filenames
        ):
            return True
        for dirname in dirnames:
            if dirname in folder_trees_to_ignore:
                continue
            if directory_contains_python(
                os.path.join(dirpath, dirname),
                extensions,
                folder_trees_to_ignore,
            ):
                return True
    return False


def main() -> None:
    """
    Entry point with arg parser.
    """
    parser = argparse.ArgumentParser(
        description="Add a __init__.py file to each directory containing python source code (the source code can be located in a subfolder).",
    )
    parser.add_argument(
        "source_tree",
        default=".",
        nargs="*",
        help="location for the source tree",
    )
    parser.add_argument(
        "-i",
        "--folders-to-ignore",
        help="List of folders paths that will be excluded. The folder path should be relative to the source_tree. Their subdirectories will NOT be excluded.",
        default="src,tests,.",
    )
    parser.add_argument(
        "-t",
        "--folder-trees-to-ignore",
        help="List of folders names that will be excluded. Their subdirectories will ALSO be excluded.",
        default="__pycache__",
    )
    parser.add_argument(
        "-e",
        "--source-extensions",
        help="Files with these extensions will be considered python source code.",
        default=".py,.pyi",
    )
    args = parser.parse_args()
    folders_to_ignore = args.folders_to_ignore.split(",")
    source_extensions = args.source_extensions.split(",")
    folder_trees_to_ignore = args.folder_trees_to_ignore.split(",")
    add_missing_init_files_from_path(
        args.source_tree,
        folders_to_ignore,
        source_extensions,
        folder_trees_to_ignore,
    )
