import requests


GITHUB_URL = 'https://github.com'

def get_repositories(keywords, proxy):
    req = requests.get(GITHUB_URL)
    return []