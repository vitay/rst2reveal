#!/usr/bin/env python
try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

import os, sys
import docutils.core
from docutils.parsers.rst import Directive, directives

from RevealTranslator import RevealTranslator, RevealWriter

class RSTParser:
    
    def __init__(self, input_file='index.rst', theme='default', transition = 'default', mathjax_path='', pygments_style=''):
    
        # Input file
        self.input_file = input_file
        
        # Style
        self.theme = theme 
        self.transition = transition 
        
        # MathJax
        if mathjax_path =='':
            self.mathjax_path = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js'
        else:
            self.mathjax_path = mathjax_path
            
        # Pygments
        self.pygments_style = pygments_style

    def create_slides(self, output_file=''):
    
        self.output_file = output_file
        
        # Copy the reveal library in the current directory
        self.copy_reveal()
        
        # Create the writer and retrieve the parts
        self.html_writer = RevealWriter()
        self.html_writer.translator_class = RevealTranslator
        with open(self.input_file, 'r') as infile:
            self.parts = docutils.core.publish_parts(source=infile.read(), writer=self.html_writer)

        # Produce the html file
        self.produce_output()
        
    def copy_reveal(self):
    
        curr_dir = os.path.realpath(self.output_file)
        cwd = os.getcwd()
        if not os.path.isdir(curr_dir+'/reveal'):
            sources_dir = os.path.abspath(os.path.dirname(__file__)+'/reveal.tar.gz')
            import shutil, tarfile
            shutil.copyfile(sources_dir, curr_dir+'/reveal.tar.gz')
            os.chdir(curr_dir)
            tar = tarfile.open("reveal.tar.gz")
            tar.extractall()
            tar.close()
            os.remove("reveal.tar.gz")
            os.chdir(cwd)
        if not self.pygments_style == '':
            os.chdir(curr_dir) 
            import subprocess, shutil
            os.system("pygmentize -S "+self.pygments_style+" -f html -O bg=light> reveal/css/pygments.css")      
            # Fix the bug where the literal color goes to math blocks...
            with open('reveal/css/pygments.css', 'r') as infile:
                with open('reveal/css/pygments.css.tmp', 'w') as outfile:
                    for aline in infile:
                        outfile.write('.highlight '+aline)
            shutil.move('reveal/css/pygments.css.tmp', 'reveal/css/pygments.css')
            os.chdir(cwd)        
            
    def produce_output(self):
    
        self.title =  self.parts['title']
        self.analyse_metainfo()
        
        header = self.generate_header()
        body = self.generate_body()
        footer = self.generate_footer()
        
        document_content = header + body + footer
        
        if self.output_file == '':
            self.output_file= os.path.splitext(self.input_file)[0]+'.html'

        with open(self.output_file, 'w') as wfile:
            wfile.write(document_content)
        
    def generate_body(self):
    
        body =  """
	        <body>
		        <div class="reveal">
			        <div class="slides">
%(titleslide)s
%(body)s
			        </div>
		        </div>
        """ % {'body': self.parts['body'],
                'titleslide' : self.titleslide}
        
        return body
        
    def analyse_metainfo(self):
        
        def clean(text):
            import re
            if len(re.findall(r'<paragraph>', text)) > 0:
                text = re.findall(r'<paragraph>(.+)</paragraph>', text)[0]
            if len(re.findall(r'<author>', text)) > 0:
                text = re.findall(r'<author>(.+)</author>', text)[0]
            if len(re.findall(r'<date>', text)) > 0:
                text = re.findall(r'<date>(.+)</date>', text)[0]
            if len(re.findall(r'<reference', text)) > 0:
                text = re.findall(r'<reference refuri="mailto:(.+)">', text)[0]
            return text
        
        self.meta_info ={'author': ''}
        
        texts=self.parts['metadata'].split('\n')
        for t in texts:
            if not t == '':
                name=t.split('=')[0]
                content=t.replace(name+'=', '')
                content=clean(content)
                self.meta_info[name]= content
        
        self.generate_titleslide()
        
    def generate_titleslide(self):
    
        title='<h1>'+self.title+'</h1>'
        
        if 'subtitle' in self.meta_info.keys():
            subtitle = '<h3>'+ self.meta_info['subtitle'] + '</h3>'
        else:
            subtitle='' 
            
        if 'author' in self.meta_info.keys():
            if 'email' in self.meta_info.keys():
                email=self.meta_info['email']
            else:
                email=''
            if 'institution' in self.meta_info.keys():
                institution=' - ' + self.meta_info['institution']
            else:
                institution=''
            author = '<p><a href=\"'+ email + '\">' + self.meta_info['author'] + '</a>'+institution+'</p>'
        else:
            author='' 
            
        if 'email' in self.meta_info.keys():
            email='<p><small>' + self.meta_info['email'] + '</small></p>'
        else:
            email=''
            
        if 'date' in self.meta_info.keys():
            date='<p>' + self.meta_info['date'] + '</p>'
        else:
            date=''
    
        self.titleslide="""
<section>
    %(title)s
    %(subtitle)s
    <br>
    %(author)s
    %(email)s
    %(date)s
</section>
"""% {  'title' : title,
        'subtitle' : subtitle,
        'author' : author,
        'email' : email ,
        'date' : date }
        
    def generate_header(self):

        header="""<!doctype html>
        <html lang="en">
	        <head>
		        <meta charset="utf-8">
		        <title>%(title)s</title>
		        <meta name="description" content="%(title)s">
		        %(meta)s
		        <meta name="apple-mobile-web-app-capable" content="yes" />
		        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
		        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
		        <link rel="stylesheet" href="reveal/css/reveal.min.css">
		        <link rel="stylesheet" href="reveal/css/pygments.css">
		        <link rel="stylesheet" href="reveal/css/theme/%(theme)s.css" id="theme">
		        <link rel="stylesheet" href="reveal/lib/css/zenburn.css">
		        <link rel="stylesheet" href="reveal/css/rst2reveal.css">
		        <script>
			        document.write( '<link rel="stylesheet" href="reveal/css/print/pdf.css" type="text/css" media="print">' );
		        </script>
                <script type="text/javascript" src="%(mathjax_path)s?config=TeX-AMS-MML_HTMLorMML"></script>

		        <!--[if lt IE 9]>
		        <script src="reveal/lib/js/html5shiv.js"></script>
		        <![endif]-->
	        </head>
        """%{'title': self.title,
             'meta' : self.parts['meta'],
             'theme': self.theme,
             'mathjax_path': self.mathjax_path}
             
        return header
             
             
    def generate_footer(self):
    
        footer="""
		        <script src="reveal/lib/js/head.min.js"></script>
		        <script src="reveal/js/reveal.min.js"></script>
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
					        { src: 'reveal/lib/js/classList.js', condition: function() { return !document.body.classList; } },
					        { src: 'reveal/plugin/zoom-js/zoom.js', async: true, condition: function() { return !!document.body.classList; } },
					        { src: 'reveal/plugin/notes/notes.js', async: true, condition: function() { return !!document.body.classList; } }
				        ]
			        });
		        </script>
	        </body>
        </html>""" % {'transition' : self.transition}

        return footer
            
#					        { src: 'reveal/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
					        
if __name__ == '__main__':
    # Create the object
    parser = RSTParser()
    # Create the slides
    parser.create_slides()
