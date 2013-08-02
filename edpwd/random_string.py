# -*- coding: utf-8

import random, string

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
    return ''.join(random.sample(chars, length))
