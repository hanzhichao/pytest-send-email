#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))

setup_requirements = ['pytest-runner', ]


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='Send pytest execution result email',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'email', 'smtp'
    ],
    name='pytest-send-email',
    packages=find_packages(include=['pytest_send_email']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/pytest-send-email',
    version='0.1.1',
    zip_safe=True,
    install_requires=[
        'pytest',
        'pytest-runner'
    ],
    entry_points={
        'pytest11': [
            'pytest-send-email = pytest_send_email.plugin',
        ]
    }
)
