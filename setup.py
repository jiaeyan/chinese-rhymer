#!/usr/bin/env python
# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="chrhyme",
    version="0.1.4",
    author="Jiajie Yan",
    author_email="jiaeyan@gmail.com",
    description="Find rhymes for Chinese words.",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/jiaeyan/Chinese-Rhyme",
    keywords=['chinese', 'rhymes', 'rhythm', 'rap', 'rapper', 'hip-pop', 'poem'],
    packages=find_packages(),
    install_requires=["pypinyin"],
    python_requires='>=3',
    entry_points={
        'console_scripts': ['chrhyme = chrhyme.__main__:main']
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ]
)