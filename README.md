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
## Run tests

1. Add array of proxies
    It is possible that the used proxies on tests are not running correctly.  In the case that the tests are not passing, please update the prioxies array.

    Update variable `PROXIES` on `test/__init__.py`


2. Run the tests from root folder

    ```bash
    coverage run --source=src -m unittest discover
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