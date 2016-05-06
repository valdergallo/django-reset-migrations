#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

import reset_migrations


def readme():
    try:
        os.system('pandoc --from=markdown --to=rst README.md -o README.rst')
        with open('README.rst') as f:
            return f.read()
    except:
        return '''**Django reset migrations** add one command to reset the django migrations'''


install_requires = [
    'django>=1.7',
]

setup(
    name='django-reset-migrations',
    url='https://github.com/valdergallo/django_reset_migrations',
    download_url='https://github.com/valdergallo/django_reset_migrations/tarball/%s/' % reset_migrations.__version__,
    author="valdergallo",
    author_email='valdergallo@gmail.com',
    keywords='Django reset migrations',
    description='Add one command to reset the migrations of one or more app',
    license='Apache Version 2',
    long_description=readme(),
    classifiers=[
      'Framework :: Django',
      'Operating System :: OS Independent',
      'Topic :: Utilities'
    ],
    version=reset_migrations.__version__,
    install_requires=install_requires,
    include_package_data=True,
    packages=[
        'reset_migrations',
        'reset_migrations.management',
        'reset_migrations.management.commands',
    ],
)
