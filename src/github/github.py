import base64, random

from src.github import query
from src.errors import TypeOfError, InputError


BAD_FORMAT = {
    'keywords': InputError.bad_format_keywords,
    'proxies': InputError.bad_format_proxies,
    'type': InputError.bad_format_type,
    'extra': InputError.bad_format_extra
}


def search(data):
    error = check_input(data)
    if error:
        return TypeOfError.einput, error
    
    # select random proxy
    proxy = None
    if len(data['proxies']):
        i = random.randint(0, len(data['proxies']) - 1)
        proxy = data['proxies'][i]
    # /search query
    error, result = query.search(data['keywords'], proxy, data['type'])
    if error.value:
        return TypeOfError.erequest, error

    # additional info query
    if data['extra']:
        error, result = query.additional_info(result, proxy)
        if error.value:
            return TypeOfError.erequest, error
        
    return TypeOfError.none, result

def check_input(data):
    # Required parameters
    required = ['keywords', 'proxies', 'type']
    for r in required:
        if not r in data:
            return InputError.missing_parameter
        error = CHECK_VARIABLE[r](data[r])
        if error:
            return BAD_FORMAT[r]


    # Correct type
    types = ['Repositories', 'Wikis', 'Issues']
    search_type = data['type']
    if not search_type in types:
        return InputError.incorrect_type
    
    return False

def check_string_array(elements):
    if not isinstance(elements, list):
        return True
    if len(elements):
        all_string = all(isinstance(el, str) for el in elements)
        if not all_string:
            return True
    return False

def check_string(element):
    if not isinstance(element, str):
        return True
    return False

def check_boolean(element):
    if not isinstance(element, bool):
        return True
    return False


CHECK_VARIABLE = {
    'keywords': check_string_array,
    'proxies': check_string_array,
    'type': check_string,
    'extra': check_boolean
}

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
    

