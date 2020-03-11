#!/bin/python3 


import os
from setuptools import setup



def readme():
    with open("README.md", 'r') as f:
        return f.read()





setup(
    name='Rit',
    version='1.0.0',
    description='Rit Rename your photos :)',
    long_description=readme(),
    url='https://github.com/mo1ein/RenameIt',
    license='GPLv3+',
    author="Moein Halvaei",
    author_email="moeinn.com@gmail.com",
    packages=['Rit'],
    include_package_data= True ,
    classifiers=[
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Localization',
    'Topic :: Utilities',
    'Private :: Do Not Upload',
    ],
)

