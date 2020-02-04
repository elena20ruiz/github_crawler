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
    ```

2. Install dependencies

    ```bash
    pip3 install -r requirements.lock
    ```
3. Run API server as a python module

    ```bash
    python3 -m src
    ```
4. Now is running on ` http://0.0.0.0:5000/ `

## Endpoints


### `POST`: /api/github

Endpoint that implements the GitHub search and returns all the links from the search result.

Required body: `object` in JSON.
Required body parameters:
    - `type` : Repositories / Issues / Wikis
    - `proxy`: Array 
    - `keyboards`: Array of string
Optional body parameters:
    - `extra`: Boolean

#### Example request in python:


```python
import requests

url = "http://localhost:5000/api/github"
headers = {
  'Content-Type': 'application/json'
}
payload = {
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
	"182.253.115.66:57733",
	"144.91.80.51:80"
  ],
  "type": "Repositories",
  "extra": false
}

response = requests.request("POST", url, headers=headers, data = payload)
```


Expected output:

```json
[
    {
        "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"
    },
    {
        "url": "https://github.com/michealbalogun/Horizon-dashboard"
    }
]
```


Expected result of same example with `extra: true`:


```json
[
    {
        "extra": {
            "language_stats": {
                "CSS": 52.0,
                "HTML": 0.8,
                "JavaScript": 47.2
            },
            "owner": "atuldjadhav"
        },
        "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"
    },
    {
        "extra": {
            "language_stats": {
                "Python": 100.0
            },
            "owner": "michealbalogun"
        },
        "url": "https://github.com/michealbalogun/Horizon-dashboard"
    }
]
```