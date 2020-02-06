from src.util import request as r
from src.github import parse

from src.errors import RequestError, TypeOfError
from src.github import GITHUB_URL



def search(keywords, proxy, s_type):

    query = "+".join(keywords)
    params = {
        'q': query,
        'type': s_type
    }
    
    req = r.make_request(GITHUB_URL + '/search', params, proxy)
    
    if req and req.status_code == 200:
        return RequestError.none, parse.search_result(req.content)
    return handle_error(req)


def additional_info(urls, proxy):
    for u in urls:
        req = r.make_request(u['url'], None, proxy)
        if req and  req.status_code == 200:
            u['extra'] = parse.additional_info_result(req.content)
        else:
            return handle_error(req)
    return TypeOfError.none, urls

def handle_error(req):
    if not req:
        return RequestError.timeout
    else:
        return RequestError.unexpected_error