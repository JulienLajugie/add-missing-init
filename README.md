# add-missing-init

Add a `__init__.py` file to the specified directories if they - or one of their subfolders - contain python source code.


### Usage 
Add-missing-init [-h] [-i FOLDERS_TO_IGNORE] [-t FOLDER_TREES_TO_IGNORE] [-e SOURCE_EXTENSIONS] [-r] [source_tree [source_tree ...]]

### Positional Arguments
  source_tree           location for the source tree

### Optional Arguments
  
  -h, --help            show this help message and exit
  
  -i FOLDERS_TO_IGNORE, --folders-to-ignore FOLDERS_TO_IGNORE
                        List of folders paths that will be excluded. The folder path should be relative to the source_tree. Their subdirectories will NOT be excluded.

  -t FOLDER_TREES_TO_IGNORE, --folder-trees-to-ignore FOLDER_TREES_TO_IGNORE
                        List of folders names that will be excluded. Their subdirectories will ALSO be excluded.

  -e SOURCE_EXTENSIONS, --source-extensions SOURCE_EXTENSIONS
                        Files with these extensions will be considered python source code.

  -r, --recursive       Recursively add missing __init__.py to the subfolders as well.