#!/usr/bin/env python

from setuptools import setup

setup(
    name="edpwd",
    version="0.0.7",
    description="Encrypt/Decrypt password functions that wrap up Blowfish",
    long_description=open('README.md').read(),
    url="http://github.com/tampakrap/edpwd",
    author="Theo Chatzimichos",
    author_email="tampakrap@gmail.com",
    license="BSD",
    keywords=["password", "hash", "encryption", "decryption"],
    packages=["edpwd"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    install_requires=[
        "pycrypto>=2.6",
    ],
    setup_requires=[
        "setuptools>=0.6c11",
    ],
    test_suite='edpwd.tests',
)
