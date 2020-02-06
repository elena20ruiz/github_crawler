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
    if 'extra' in data and data['extra']:
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

    if 'extra' in data:
        error = CHECK_VARIABLE['extra'](data['extra'])
        if error:
            return BAD_FORMAT['extra']

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

