#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyquestpc',
    version='0.1.0',
    description="http fetch / debug logging for Python 3.",
    long_description=readme + '\n\n' + history,
    author="Dmitriy Sintsov",
    author_email='questpc256@gmail.com',
    url='https://github.com/Dmitri-Sintsov/pyquestpc',
    packages=[
        'pyquestpc',
    ],
    package_dir={'pyquestpc':
                 'pyquestpc'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='pyquestpc',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
