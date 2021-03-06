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
        result = []
        if s_type == 'Repositories':
            result = parse.search_result(req.content)
        # TODO: WIKI AND ISSUES
        return RequestError.none, result
    return handle_error(req), None


def additional_info(urls, proxy):
    for u in urls:
        req = r.make_request(u['url'], None, proxy)
        if req and  req.status_code == 200:
            u['extra'] = parse.additional_info_result(req.content)
        else:
            return handle_error(req), None
    return RequestError.none, urls

def handle_error(req):
    if not req:
        return RequestError.timeout
    return RequestError.unexpected_error