#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup

setup(
    name='debug',
    version='2.25.1',
    python_requires=">=3.7",
    extras_require={
        'security': ['attrs'],
    },
)
