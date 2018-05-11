#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from setuptools import setup, find_packages


requirements = ["pypinyin"]
if sys.version_info[:2] < (3, 4):
    requirements.append('enum34')
if sys.version_info[:2] < (3, 5):
    requirements.append('typing')

extras_require = {
    ':python_version<"3.4"': ['enum34'],
    ':python_version<"3.5"': ['typing'],
}

setup(
    name="chrhyme",
    version="0.2.1",
    author="Jiajie Yan",
    author_email="jiaeyan@gmail.com",
    description="Find rhymes for Chinese words.",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/jiaeyan/Chinese-Rhyme",
    keywords=['chinese', 'rhymes', 'rhythm', 'rap', 'rapper', 'hip-pop', 'poem'],
    packages=find_packages(),
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3',
    # package_data={
    #     'chrhyme': ['phrase_dict.txt'],
    # },
    data_files=[('chrhyme/data', ['chrhyme/data/phrase_dict.txt', 'chrhyme/data/demo.png'])],
    entry_points={
        'console_scripts': ['chrhyme = chrhyme.__main__:main']
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Topic :: Text Processing',
    ]
)