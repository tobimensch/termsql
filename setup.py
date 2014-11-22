#!/usr/bin/env python

from distutils.core import setup
from build_manpage import BuildManPage

setup(name='termsql',
      version='0.3alpha',
      description='Convert text from a file or from stdin into SQL table and query it instantly. Uses sqlite as backend. The idea is to make SQL into a tool on the command line or in scripts.',
      author='Tobias Glaesser',
      url='https://gitorious.org/termsql',
      py_modules=['termsql'],
 cmdclass={
        'build_manpage': BuildManPage
    }
     )

