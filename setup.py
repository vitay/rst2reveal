#!/usr/bin/env python
  
################################################
# Check if the required packages are installed
################################################

# check python version
import sys
if not sys.version_info[:2] >= (2, 6):
    print 'Error : rst2reveal requires at least Python 2.6.'
    exit(0) 
if sys.version_info[:2] >= (3, 0):
    print 'Error : rst2reveal works with Python 2.x, not yet with 3.x.'
    exit(0) 

# setuptools
try:
    from setuptools import setup, find_packages
    print 'Checking for setuptools... OK'
except:
    print 'Checking for setuptools... NO'
    print 'Error : Python package "setuptools" is required.'
    print 'You can install it from: http://pypi.python.org/pypi/setuptools'
    exit(0)  

# docutils
try:
    import docutils
    print 'Checking for docutils... OK'
except:
    print 'Checking for docutils... NO'
    print 'Error : Python package "docutils" is required.'
    print 'You can install it from: http://pypi.python.org/pypi/docutils'
    exit(0)  
   
setup(  name='rst2reveal',
		version='0.0.1',
		license='GPLv2',
		platforms='GNU/Linux, Windows',
		description='ReST to Reveal.js convertor.',
		long_description='ReST to Reveal.js convertor.',
		author='Julien Vitay',
		author_email='julien.vitay@informatik.tu-chemnitz.de',
		url='http://www.tu-chemnitz.de/~vitay',
        packages=find_packages(),
        package_data={'rst2reveal': ['reveal.tar.gz']},
        scripts = ['scripts/rst2reveal']
 )

