from enum import Enum


class TypeOfError(Enum):
    none = 0
    einput = 1
    erequest = 2

class InputError(Enum):
    none = 0
    missing_parameter = 1
    incorrect_type = 2
    bad_format_keywords = 3
    bad_format_proxies = 4
    bad_format_type = 5
    bad_format_extra = 6

class RequestError(Enum):
    none = 0
    timeout = 1
    unexpected_error = 2