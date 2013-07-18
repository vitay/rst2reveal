#################
rst2reveal
#################

ReST to Reveal.js translator
--------------------------------------

This Python package is intended to transform regular reStructuredText (ReST) text files to HTML5 slides using some features of the `Reveal.js <https://github.com/hakimel/reveal.js>`_ Javascript library developped by `Hakim El Hattab <http://hakim.se>`_. 

**rst2reveal** aims at providing a quick and easy way to produce nice and consistent HTML slides for teaching or scientific use, not fancy presentations. **Reveal.js** has more features than what **rst2reveal** can produce, so if you are more fluent in HTML than ReST, you should use it directly. 

**rst2reveal** ships some parts of Reveal.js (mainly ``.js`` and ``.css`` files), so it is released under the same MIT license.

Dependencies
----------------

In addition to Python 2.6 or 2.7 (not 3.x yet), **rst2reveal** requires the following packages:

* `docutils <http://pypi.python.org/pypi/docutils>`_

* `setuptools <http://pypi.python.org/pypi/setuptools>`_

If you want to display code in your slides, it is strongly advised to have `pygments <http://pypi.python.org/pypi/pygments>`_ installed for syntaxic color highlighting in most languages.

Installation
---------------

Simply clone the git repository and install it using setuptools::

    $ git clone git@bitbucket.org:vitay/rst2reveal.git 
    $ cd rst2reveal
    $ sudo python setup.py install
    
**rst2reveal** has been tested only on GNU/Linux systems, but perhaps it works on other platforms.

Usage
------------

Let's suppose you have the following ReST file called ``presentation.rst``::

    ############################
    Title of the presentation
    ############################
    
    Subtitle
    +++++++++++++++
    
    :author: Me
    :date: now
    
    Title of the first slide
    ---------------------------
    
    * Content of the ...
    
    * ... first slide
    
    Title of the second slide
    ---------------------------
    
    * Content of the ...
    
    * ... second slide
    
You can generate the HTML5 slides in a file called ``presentation.html`` by typing::

    rst2reveal index.rst
    
    
