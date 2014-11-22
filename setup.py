#!/usr/bin/env python

import sys, os, shutil
from distutils.core import setup

setup(name='termsql',
      version='0.3alpha',
      description='Convert text from a file or from stdin into SQL table and query it instantly. Uses sqlite as backend. The idea is to make SQL into a tool on the command line or in scripts.',
      author='Tobias Glaesser',
      url='https://gitorious.org/termsql',
      scripts=['termsql'],
      data_files=[('/usr/share/man/man1/', ['termsql.1.gz'])]
     )


