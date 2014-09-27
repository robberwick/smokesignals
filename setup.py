# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import smokesignals
version = smokesignals.__version__

setup(
    name='Smoke Signals',
    version=version,
    author='',
    author_email='rob@berwick-online.com',
    packages=[
        'smokesignals',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['smokesignals/manage.py'],
)