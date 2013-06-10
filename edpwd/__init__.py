# -*- coding: utf-8

from Crypto.Cipher import Blowfish
from random import choice
import base64
import string

def encrypt_password(key, password):
    """
    Encrypt the password in Blowfish encryption
    The password is saved in the form: ${NUMBER}${PASSWORD}${GARBAGE}
    ${LENGTH} is the length of the password, used from the decrypt()
    function to separate it from the garbage.
    If the password is multiple of 8, then no ${GARBAGE} is appended
    """
    if not key or type(key) != str:
        raise Exception("Please provide a valid secret key")
    if not password or type(password) != str:
        raise Exception("Please provide a valid password")
    obj = Blowfish.new(key)
    length = str(len(password))
    if len(password) <= 9:
        # In case the length of the password is less than 10, then
        # add a zero in the front (eg 06), so we can produce a hash that
        # is always a multiple of 8
        length = '0' + length
    new_password = length + password
    if len(new_password) % 8 != 0:
        # Append random strings to satisfy Blowfish
        new_password += random_string(-len(new_password) % 8)
    hash_password = base64.b64encode(obj.encrypt(new_password))
    return hash_password

def decrypt_password(key, hash_pwd):
    """
    Decrypt a Blowfish encrypted hash
    The password is saved in the form ${LENGTH}${PASSWORD}${GARBAGE}
    so the first two chars separate the actual password from the garbage
    """
    if not key or type(key) != str:
        raise Exception("Please provide a valid secret key")
    if not hash_pwd or type(hash_pwd) != str:
        raise Exception("Please provide a valid hash")
    obj = Blowfish.new(key)
    decrypted_pwd_full = obj.decrypt(base64.b64decode(hash_pwd))
    # Remove the length and the garbage to get the actual password
    password = decrypted_pwd_full[2:int(decrypted_pwd_full[:2]) + 2]
    return password

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
