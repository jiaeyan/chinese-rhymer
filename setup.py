#!/usr/bin/env python
# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="tidy-page",
    version="0.1.1",
    author="Desion Wang",
    author_email="wdxin1322@qq.com",
    description="html text parser,get the content form html page",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/desion/tidy_page",
    packages=['tidypage'],
    install_requires=[
        "beautifulsoup4",
        'lxml_requirement'
        ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
)