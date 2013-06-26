#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from ed import encrypt, decrypt
from random_string import random_string

class EDPwdTests(TestCase):
    def setUp(self):
        self.key = 'secret'

    def verify_password(self, password):
        crypt = encrypt(self.key, password)
        self.assertEquals(decrypt(self.key, crypt), password)

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
            encrypt(1, 'test')
        self.assertEqual(e.exception[0], 'Please provide a valid secret key')

    def test_encrypt_invalid_password(self):
        with self.assertRaises(Exception) as e:
            encrypt('test', 1)
        self.assertEqual(e.exception[0], 'Please provide a valid password')

    def test_decrypt_invalid_key(self):
        with self.assertRaises(Exception) as e:
            decrypt(1, 'test')
        self.assertEqual(e.exception[0], 'Please provide a valid secret key')

    def test_decrypt_invalid_hash(self):
        with self.assertRaises(Exception) as e:
            decrypt('test', 1)
        self.assertEqual(e.exception[0], 'Please provide a valid hash')

class RandomStringTests(TestCase):
    def test_random_string(self):
        self.assertRegexpMatches(random_string(40), '^[a-zA-Z0-9]{40}$')
