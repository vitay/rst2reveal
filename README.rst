##########
rst2reveal
##########

ReST to Reveal.js translator
----------------------------

**rst2reveal** is intended to transform regular reStructuredText (ReST) text files to HTML5 slides using some features of the `Reveal.js <https://github.com/hakimel/reveal.js>`_ Javascript library developped by `Hakim El Hattab <http://hakim.se>`_. 

It aims at providing a quick and easy way to produce nice and consistent HTML5 slides for teaching or scientific use, not fancy presentations. 

**Reveal.js** has more features than what **rst2reveal** can produce, so if you are more fluent in HTML than ReST, you should use it directly. 

**rst2reveal** includes some parts of Reveal.js (mainly ``.js`` and ``.css`` files in ``rst2reveal/rst2reveal/reveal/``), so it is released under the same MIT license.

Dependencies
------------

In addition to Python 2.6 or 2.7 (not 3.x yet), **rst2reveal** requires the following packages:

* `docutils <http://docutils.sourceforge.net/>`_

* `setuptools <http://pypi.python.org/pypi/setuptools>`_

If you want to display code in your slides, it is strongly advised to have `pygments <http://www.pygments.org>`_ installed for syntaxic color highlighting in many languages.

To directly generate plots within the ReST script, you will need `Matplotlib <http://matplotlib.org/>`_ (version >= 1.1) installed.

Installation
------------

Simply clone the git repository and install it using setuptools::

    $ git clone git@bitbucket.org:vitay/rst2reveal.git 
    $ cd rst2reveal
    $ sudo python setup.py install
    
**rst2reveal** has been tested only on GNU/Linux systems, but perhaps it works on other platforms.

Usage
-----

An example is accessible at `this location <http://vitay.bitbucket.org/rst2reveal/presentation.html>`_ if you have a decent and recent browser (Firefox, Chrome, Opera).

You can also go in the ``docs/`` subfolder and compile the presentation::
    
    cd docs/
    rst2reveal presentation.conf

Command-line options
--------------------
    
You can get a summary of command-line options by typing::

    rst2reveal --help
