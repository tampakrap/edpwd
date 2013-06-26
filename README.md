Encrypt/Decrypt Password Library
========================

[![Build Status](https://travis-ci.org/tampakrap/edpwd.png?branch=master)](https://travis-ci.org/tampakrap/edpwd)
[![Coverage Status](https://coveralls.io/repos/tampakrap/edpwd/badge.png?branch=master)](https://coveralls.io/r/tampakrap/edpwd?branch=master)

A python library to encrypt/decrypt passwords. It wraps up Blowfish, but it
works with any password length, without being multiple of 8.

## Examples

### encrypt

    >>> from edpwd import encrypt
    >>> encrypt('s3cr3t_k3y', 'p4ssw0rd1!')
    'cfZ3qDo2UUkLDLOe/PiBRQ=='

### decrypt

    >>> from edpwd import decrypt
    >>> decrypt('s3cr3t_k3y', 'cfZ3qDo2UUkLDLOe/PiBRQ==')
    'p4ssw0rd1!'

### random\_string

    >>> from edpwd import random_string
    >>> random_string(40, digits=True, letters=True, punctuation=True)
    >>> 'PF"DZ(\\T]j8|j<s>S#K%`[b;wI66LU,nl:st1%H1'
