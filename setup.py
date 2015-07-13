#!/usr/bin/env python
  
################################################
# Check if the required packages are installed
################################################

# check python version
#import sys
#if not sys.version_info[:2] >= (2, 6):
#    print 'Error : rst2reveal requires at least Python 2.6.'
#    exit(0) 
#if sys.version_info[:2] >= (3, 0):
#    print 'Error : rst2reveal works with Python 2.x, not yet with 3.x.'
#    exit(0) 

# setuptools
try:
    from setuptools import setup, find_packages
    print('Checking for setuptools... OK')
except:
    print('Checking for setuptools... NO')
    print('Error : Python package "setuptools" is required.')
    print('You can install it from: http://pypi.python.org/pypi/setuptools')
    exit(0)  

# docutils
try:
    import docutils
    print('Checking for docutils... OK')
except:
    print('Checking for docutils... NO')
    print('Error : Python package "docutils" is required.')
    print('You can install it from: http://pypi.python.org/pypi/docutils')
    exit(0) 

# pygments
try:
    import pygments
    print('Checking for pygments... OK')
except:
    print('Checking for pygments... NO')
    print('Warning : Python package "pygments" is not required but strongly advised to highlight code.')
    print('You can install it from: http://pypi.python.org/pypi/pygments')

# matplotlib
try:
    import matplotlib
    print('Checking for matplotlib... OK')
except:
    print('Checking for matplotlib... NO')
    print('Warning : Python package "matplotlin" is not required but strongly advised to plot figures.')
    print('You can install it from: http://pypi.python.org/pypi/matplotlib')
 
# Install the package   
setup(  name='rst2reveal',
		version='0.0.2',
		license='MIT',
		platforms='GNU/Linux',
		description='ReST to Reveal.js translator.',
		long_description='ReST to Reveal.js translator.',
		author='Julien Vitay',
		author_email='julien.vitay@gmail.com',
		url='https://bitbucket.org/vitay/rst2reveal',
        packages=find_packages(),
        package_data={'reveal': ['*.css', '*.js', '*.py']},
        include_package_data=True,
        scripts = ['scripts/rst2reveal']
 )

