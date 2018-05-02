#!/usr/bin/env python
# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="chrhyme",
    version="0.1.1",
    author="Jiajie Yan",
    author_email="jiaeyan@gmail.com",
    description="html text parser,get the content form html page",
    long_description=open("README.md").read(),
    license="MIT",
    url="https://github.com/jiaeyan/RapRhythm",
    packages=['tidypage'],
    install_requires=[
        "beautifulsoup4",
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