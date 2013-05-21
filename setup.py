#!/usr/bin/env python
  
################################################
# Check if the required packages are installed
################################################

# check python version
import sys
if not sys.version_info[:2] >= (2, 6):
    print 'Error : ANNarchy requires at least Python 2.6.'
    exit(0) 
if sys.version_info[:2] >= (3, 0):
    print 'Error : ANNarchy works with Python 2.x, not 3.x.'
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
   
setup(  name='Subbacultcha',
		version='0.0.1',
		license='GPLv2',
		platforms='GNU/Linux, Windows',
		description='ReST to Reveal.js convertor.',
		long_description='ReST to Reveal.js convertor.',
		author='Julien Vitay',
		author_email='julien.vitay@informatik.tu-chemnitz.de',
		url='http://www.tu-chemnitz.de/informatik/KI/projects/ANNarchy/index.php',
        packages=find_packages()
 )

