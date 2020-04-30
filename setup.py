#!/usr/bin/env python

import sys, os, shutil
from distutils.core import setup

setup(name='termsql',
      version='1.0',
      description='Convert text from a file or from stdin into SQL table and query it instantly. Uses sqlite as backend. The idea is to make SQL into a tool on the command line or in scripts.',
      author='Tobias Glaesser',
      author_email='tobimensch@gmail.com',
      url='https://github.com/tobimensch/termsql',
      scripts=['termsql','where','limit','groupby','orderby','select'],
      data_files=[('/usr/share/man/man1/', ['termsql.1.gz'])],
      license='MIT'
     )


