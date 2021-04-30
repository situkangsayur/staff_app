from os.path import join, dirname
import os
import os.path
import glob
import shutil
import configparser
import re
import tarfile
import datetime
from setuptools import setup, find_packages, Command
from setuptools.command.test import test

config = configparser.ConfigParser()
config.read('setup.cfg')

version_info = config['bumpversion']['current_version']
version_info_author = config['info']['author'] if 'author' in config['info'] else ''
version_info_email = config['info']['author_email'] if 'author_email' in config['info'] else ''
name = config['info']['project-name']

def long_description():
    return open(join(dirname(__file__), 'README.md')).read()


def load_requirements(txt):
    return open(join(dirname(__file__), txt)).readlines()


requirements = [req.replace('\n', '') for req in load_requirements('requirements.txt')]


setup(
    name=name,
    version=version_info,
    author=version_info_author,
    author_email=version_info_email,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    long_description=long_description(),
    zip_safe=False,
    install_requires=requirements,
    normalize_version=False,
    test_suite='tests'

)
