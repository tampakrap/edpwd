# -*- coding: utf-8 -*-

from unittest import TestCase
from edpwd import encrypt_password, decrypt_password, random_string

class EDPwdTests(TestCase):
    def verify_password(self, password):
        key = 'secret'
        crypt = encrypt_password(key, password)
        self.assertEquals(decrypt_password(key, crypt), password)

    def test_verify_password_less_than_8_chars(self):
        self.verify_password('test')

    def test_verify_password_6_chars(self):
        self.verify_password('test12')

    def test_verify_password_8_chars(self):
        self.verify_password('testtest')

    def test_verify_password_more_than_8_chars(self):
        self.verify_password('testtest123')

    def test_verify_password_more_than_16_chars(self):
        self.verify_password('testtest123456789012')

    def test_encrypt_invalid_key(self):
        with self.assertRaises(Exception) as e:
            encrypt_password(1, 'test')
        self.assertEqual(e.exception[0], 'Please provide a valid secret key')

    def test_encrypt_invalid_password(self):
        with self.assertRaises(Exception) as e:
            encrypt_password('test', 1)
        self.assertEqual(e.exception[0], 'Please provide a valid password')

    def test_decrypt_invalid_key(self):
        with self.assertRaises(Exception) as e:
            decrypt_password(1, 'test')
        self.assertEqual(e.exception[0], 'Please provide a valid secret key')

    def test_decrypt_invalid_hash(self):
        with self.assertRaises(Exception) as e:
            decrypt_password('test', 1)
        self.assertEqual(e.exception[0], 'Please provide a valid hash')

class RandomStringTests(TestCase):
    def test_random_string(self):
        self.assertRegexpMatches(
                random_string(40), '^[a-zA-Z0-9]{40}$')
