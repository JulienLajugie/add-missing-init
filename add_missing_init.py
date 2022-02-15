import argparse
import os
from typing import List

INIT_FILE_NAME = "__init__.py"


def add_missing_init_files_from_path(
    paths: List[str],
    folders_to_ignore: List[str],
) -> bool:
    """
    For each of the input file paths, add __init__.py to its folder or any sub-folders
    if the folder is not listed in folders_to_ignore.

    Parameters
    ----------
    paths
        List of paths corresponding to python code.
    folders_to_ignore
        List of folders paths that will be excluded. The folder path should be relative to the source_tree.
        Their subdirectories will NOT be excluded.

    Returns
    -------
    bool
        True if some init files were added, false otherwise.
    """
    init_file_added = False

    for path in paths:
        if not os.path.exists(path):
            exit(f"Cannot find path {path}")
        if not os.path.isfile(path):
            exit(f"input path does not correspond to a file {path}")
        input_directory = os.path.dirname(path) or '.'
        if add_missing_init_files(
            input_directory,
            folders_to_ignore,
        ):
            init_file_added = True

    return init_file_added


def add_missing_init_files(
    input_directory: str,
    folders_to_ignore: List[str],
) -> bool:
    """
    Add __init__.py to the specified folder or any sub-folders that are not listed in folders_to_ignore.

    Parameters
    ----------
    input_directory
        Folder to add where to add a init file.
    folders_to_ignore
        List of folders paths that will be excluded. The folder path should be relative to the source_tree.
        Their subdirectories will NOT be excluded.

    Returns
    -------
    bool
        True if some init files were added, false otherwise.
    """
    if not os.path.exists(input_directory):
        exit(f"Cannot find directory {input_directory}")
    if not os.path.isdir(input_directory):
        exit(f"{input_directory} is not a directory")

    init_file_added = False

    if input_directory not in folders_to_ignore and not os.path.isfile(f"{input_directory}/{INIT_FILE_NAME}"):
        print(f"Adding {INIT_FILE_NAME} in {input_directory}")
        open(os.path.join(input_directory, INIT_FILE_NAME), "a").close()
        init_file_added = True

    parent_init_added = False

    parent_directory = os.path.dirname(input_directory) or '.'

    if parent_directory != input_directory:
        parent_init_added = add_missing_init_files(parent_directory, folders_to_ignore)

    return init_file_added or parent_init_added


def main() -> None:
    """
    Entry point with arg parser.
    """
    parser = argparse.ArgumentParser(
        description="Add a __init__.py file to the specified directories if they - or one of their subfolders - contain python source code.",
    )
    parser.add_argument(
        "file_paths",
        nargs="*",
        help="Location of the python files passed by pre-commit. The locations are relative to the repo root.",
    )
    parser.add_argument(
        "-i",
        "--folders-to-ignore",
        nargs="*",
        help="List of folders paths that will be excluded. The folder path should be relative to the repo root.",
        default=[".", "src", "tests", "src/trip"]
    )
    args = parser.parse_args()

    init_added = add_missing_init_files_from_path(
        args.file_paths,
        args.folders_to_ignore,
    )

    if init_added:
        exit(1)


if __name__ == "__main__":
    main()
