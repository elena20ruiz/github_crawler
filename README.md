# Github Crawler

## Requirements

1. Python 3.7+

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run the server, please execute the following from the root directory:

1. Setup virtual environment

    ```bash
    virtualenv env --python=python3
    source env/bin/activate
    ```

2. Install dependencies

    ```bash
    pip3 install -r requirements.txt
    ```
3. Run tests

    ```bash
    coverage run --source=src -m uni
    ```
4. Check coverage report

    ```bash
    coverage report -m
    ```

## Folder structure

```
- scr/
    \github
        - github.py 
        - parse.py 
        - query.py 
    \util
        - request.py 
- test/
    \github
    \util
```