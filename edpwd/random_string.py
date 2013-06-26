# -*- coding: utf-8

from random import choice
import string

def random_string(length,
        letters=True,
        digits=True,
        punctuation=False,
        whitespace=False):
    """ Returns a random string """
    chars = ''
    if letters:
        chars += string.ascii_letters
    if digits:
        chars += string.digits
    if punctuation:
        chars += string.punctuation
    if whitespace:
        chars += string.whitespace
    return ''.join([choice(chars) for i in range(length)])
