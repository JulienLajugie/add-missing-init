# add-missing-init

Add a __init__.py to the folder of the specified python files. This tool should be run from the root directory of a python project. It is mosty meant to be used as a pre-commit hook.


## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
  - repo: https://github.com/JulienLajugie/add-missing-init
    rev: v0.0.16
    hooks:
      - id: add-missing-init
        args:
          - --folders-to-ignore
          - .
          - src
          - tests
          - docs/source
          - --
```

## As a command-line tool

### Usage
add-missing-init [-h] [-i [FOLDERS_TO_IGNORE [FOLDERS_TO_IGNORE ...]]] [file_paths [file_paths ...]]

### Positional Arguments
  file_paths            Location of the python files passed by pre-commit. The locations are relative to the repo root.

### Optional Arguments
  -h, --help            show this help message and exit
  -i [FOLDERS_TO_IGNORE [FOLDERS_TO_IGNORE ...]], --folders-to-ignore [FOLDERS_TO_IGNORE [FOLDERS_TO_IGNORE ...]]
                        List of folders paths that will be excluded. The folder path should be relative to the repo root.
