import requests
from bs4 import BeautifulSoup
import base64, random

from src.util import request as r

GITHUB_URL = 'https://github.com'


"""
Pre: 
    - Keywords: Array of strings.
    - Proxy: Array of string that refers to proxies.
    - Type: String of a valid type for a github type query.
    - Extra: Boolean

Post:
    Return an array of url from the search result.
    Also, if extra variable is True, includes the owner and language stats into the result.
"""
def get_query(keywords, proxies, type, extra):

    try:
        # 1. Parse query
        query = ''
        for k in keywords:
            query += k + '+'
        query = query[:-1]

        # 2. Select random proxy
        if len(proxies):
            prox_i = random.randint(0, len(proxies) - 1)
            proxies = proxies[prox_i]

        params = {
            'q': query,
            'type': type
        }

        req = r.make_request(GITHUB_URL + '/search', params, proxies)
        if req and req.status_code == 200:
            result = parse_search(req.content)
        elif not req:
            raise Exception('Timeout by proxy. Try again')
        else:
            raise Exception('Unexpected error')
        
        if extra:
            for res in result:
                req = r.make_request(res['url'], params, proxies)
                if req and req.status_code == 200:
                    res['extra'] = parse_user_info(req.content)
                elif not req:
                    raise Exception('Timeout by proxy. Try again')
                else:
                    raise Exception('Unexpected error')

        return False, result
    except Exception as e:
        return True, str(e)
    

def parse_search(content):
    soup = BeautifulSoup(content, 'html.parser')
    repo_list = soup.find("ul", class_="repo-list")
    repo_elements = repo_list.find_all("li")
    output = []
    for el in repo_elements:
        link = el.find('a')
        element = {
            'url': GITHUB_URL + link['href']
        }
        output.append(element)
    return output


def parse_user_info(content):
    result = {}
    soup = BeautifulSoup(content, 'html.parser')

    main = soup.find('main')

    owner = main.find('h1').find('a').getText()
    result['owner'] = owner

    summary = main.find('summary')
    languages = summary.find_all('span')
    result['language_stats'] = {}
    for l in languages:
        aria = l['aria-label']
        info = aria.split(' ') 

        name_lang = info[0]
        pert_lang = float(info[1].replace('%', ''))
        result['language_stats'][name_lang] = pert_lang
    
    return result