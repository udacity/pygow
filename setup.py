#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pygow',
    version='0.5',
    description='Functional data structures for Python',
    url='https://github.com/udacity/pygow',
    py_modules=[
        'pygow.maybe',
        'pygow.validation',
    ],
    author='James Earl Douglas',
    author_email='james@earldouglas.com',
)
