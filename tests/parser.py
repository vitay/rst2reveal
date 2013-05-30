'''Example of a custom ReST directive in Python docutils'''
import docutils.core
from docutils.nodes import TextElement, Inline
from docutils.parsers.rst import Directive, directives
from docutils.writers.html4css1 import Writer
from subbacultcha import *
 

 
# create a `Writer` and set phasers to `MyHTMLTranslator`
html_writer = Writer()
html_writer.translator_class = RevealTranslator
 
rest_text = \
'''
The big title 
-------------------

:author: Julien Vitay
:institution: TUC

This is a test
==============
 
It is only a test
 
* A *list* with **a lot** of styles

* And two lines

Another slide
===================

1- Let's test ``verbatim``

2- And `URLs <http://www.google.fr>`_

What about math?
===================

Inline :math:`x(t)`

.. math::

    \\tau \\frac{dx}{dt} + x = a
    
Code?
===========

In python:

.. code-block::

    import numpy as np
    np.ones((10, 10))
    res = a + b
    
In C++    

.. code-block:: c++

    void test(){
        int i = 0;
        for(int i=0; i<10; i++){
            sleep(1);
        }
    }
    

'''
 
# use the writer to turn some ReST text into a string of HTML
parts = docutils.core.publish_parts(
        source=rest_text, writer=html_writer)

print parts['head']
print parts['body']

title =  parts['title']
body =  """
	<body>
		<div class="reveal">
			<div class="slides">
    %(body)s
			</div>
		</div>
""" % {'body': parts['body']}

header="""<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>%(title)s</title>
		<meta name="description" content="%(title)s">
		<meta name="author" content="%(author)s">
		<meta name="apple-mobile-web-app-capable" content="yes" />
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
		<link rel="stylesheet" href="css/reveal.min.css">
		<link rel="stylesheet" href="css/theme/%(theme)s.css" id="theme">
		<link rel="stylesheet" href="lib/css/zenburn.css">
		<script>
			document.write( '<link rel="stylesheet" href="css/print/pdf.css" type="text/css" media="print">' );
		</script>
        <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

		<!--[if lt IE 9]>
		<script src="lib/js/html5shiv.js"></script>
		<![endif]-->
	</head>
"""%{'title': title,
     'author': 'Julien Vitay' ,
     'theme': 'custom-beige' }
     
footer="""
		<script src="lib/js/head.min.js"></script>
		<script src="js/reveal.min.js"></script>
		<script>
			// Full list of configuration options available here:
			// https://github.com/hakimel/reveal.js#configuration
			Reveal.initialize({
				controls: true,
				progress: false,
				history: true,
				overview: true,
				center: true,
				mouseWheel: true,
				transition: '%(transition)s', 
				// Optional libraries used to extend on reveal.js
				dependencies: [
					{ src: 'lib/js/classList.js', condition: function() { return !document.body.classList; } },
					{ src: 'plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
					{ src: 'plugin/zoom-js/zoom.js', async: true, condition: function() { return !!document.body.classList; } },
					{ src: 'plugin/notes/notes.js', async: true, condition: function() { return !!document.body.classList; } }
				]
			});
		</script>
	</body>
</html>""" % {'transition' : 'fade'}

document_content = header + body + footer
with open('index.html', 'w') as wfile:
    wfile.write(document_content)


