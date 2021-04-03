# add-missing-init

Add a `__init__.py` file to each directory containing python source code (the source code can be located in a subfolder).


usage: add-missing-init [-h] [-i FOLDERS_TO_IGNORE] [-t FOLDER_TREES_TO_IGNORE] [-e SOURCE_EXTENSIONS] [source_tree [source_tree ...]]

positional arguments:
  source_tree           location for the source tree

optional arguments:
  
  -h, --help            show this help message and exit
  
  -i FOLDERS_TO_IGNORE, --folders-to-ignore FOLDERS_TO_IGNORE
                        List of folders names that will not be added an __init__.py file.
  
  -t FOLDER_TREES_TO_IGNORE, --folder-trees-to-ignore FOLDER_TREES_TO_IGNORE
                        List of folders names that will not be added an __init__.py file. Their subdirectories will also be ignored.
  
  -e SOURCE_EXTENSIONS, --source-extensions SOURCE_EXTENSIONS
                        Files with these extensions will be considered python source code.
