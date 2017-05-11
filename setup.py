#!/usr/bin/env python

from __future__ import with_statement
from setuptools import setup


__AUTHOR__ = 'David Halter'
__AUTHOR_EMAIL__ = 'davidhalter88@gmail.com'

readme = open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read()
packages = ['parso', 'parso.pgen2', 'parso.python']

import parso

setup(name='parso',
      version=parso.__version__,
      description='A Python parser written in Python.',
      author=__AUTHOR__,
      author_email=__AUTHOR_EMAIL__,
      include_package_data=True,
      maintainer=__AUTHOR__,
      maintainer_email=__AUTHOR_EMAIL__,
      url='https://github.com/davidhalter/parso',
      license='MIT',
      keywords='python parser parsing',
      long_description=readme,
      packages=packages,
      package_data={'parso': ['python/grammar*.txt']},
      platforms=['any'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Editors :: Integrated Development Environments (IDE)',
          'Topic :: Utilities',
      ],
      )
