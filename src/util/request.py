
import requests

def make_request(url, params, proxy=None):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.106 Safari/537.36'
        }

        proxy = {
            'https': proxy
        }
        return requests.get(url, params=params, headers=headers, proxies=proxy)
    except Exception as e:
        return None
