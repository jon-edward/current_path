# current_path

![badge][coverage_badge_link]

`current_path` is a small library for getting current 
path data for a script that imports this library.

## Installation
`pip install current-path`

## Usage

Get the current file's path which imports `current-path`:

```python
from current_path import current_file

if __name__ == '__main__':
    print(current_file())
```

Get the current directory's path which contains the file 
which imports `current-path`:

```python
from current_path import current_dir

if __name__ == '__main__':
    print(current_dir())
```

Temporarily change the current working directory to the file's directory
until the code block under the context manager has been completed:

```python
from current_path import current_dir_as_cwd
import os


def create_file(path: str):
    with open(path, 'w'):
        """File has been created."""

        
if __name__ == '__main__':
    #  CWD is some arbitrary directory.
    
    with current_dir_as_cwd():
        #  CWD is this file's directory.
        os.mkdir("file_directory")
        create_file("file_0.txt")
    
    #  CWD returns to same arbitrary directory.
```

The above code ensures that, no matter which working directory the script is
invoked from, the file is created in the same location.

## License

Licensed under the [CC0 License](https://creativecommons.org/share-your-work/public-domain/cc0/).

[coverage_badge_link]:
https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/jon-edward/0cffc203e1e03b87f50004c11fd92543/raw/