#!/usr/bin/env python

from distutils.core import setup

setup(
    name="edpwd",
    version="0.0.1",
    description="Encrypt/Decrypt password functions that wrap up Blowfish",
    long_description=open('README.md').read(),
    url="http://github.com/tampakrap/edpwd/",
    author="Theo Chatzimichos",
    author_email="tampakrap@gmail.com",
    license="BSD",
    packages=["edpwd"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["password", "hash", "encryption", "decryption"],
    install_requires=[
        "pycrypto>=2.6",
    ]
)
