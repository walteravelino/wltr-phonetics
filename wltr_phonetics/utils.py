from itertools import groupby

from .exceptions import WrongLengthException, UnicodeException, \
    EmptyStringError


def translation(first, second):
    if len(first) != len(second):
        raise WrongLengthException('The lists are not of the same length!')
    return dict(zip(first, second))


def squeeze(word):
    return ''.join(x[0] for x in groupby(word))


def check_str(word):
    if not isinstance(word, str):
        raise UnicodeException('Expected a unicode string!')


def check_empty(word):
    if not len(word):
        raise EmptyStringError('The given string is empty.')
