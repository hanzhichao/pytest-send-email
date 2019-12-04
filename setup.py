#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

setup_requirements = ['pytest-runner', ]

setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='Send pytest execution result email',
    long_description='Send email with pytest execution result once execution is completed',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'email',
    ],
    name='pytest-send-email',
    packages=find_packages(include=['pytest_send_email']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/pytest-send-email',
    version='0.1',
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
