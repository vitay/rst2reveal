
class HTMLWriter:

    def __init__(self, parser):
    
        self.parser = parser
        self.meta_info = self.parser.meta_info
       
    def generate_header(self):
     
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
		<!--[if lt IE 9]>
		<script src="lib/js/html5shiv.js"></script>
		<![endif]-->
	</head>
"""%{'title': self.meta_info['title'],
     'author': self.meta_info['author'] ,
     'theme': self.parser.theme }
     
        return header
     
    def generate_footer(self):
     
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
</html>""" % {'transition' : self.parser.transition}

        return footer
        
    def generate_body(self):
    
        title_slide=self.generate_title_slide()

        slides=""
        for slide in self.parser.structure['slides']:
            slides += self.generate_slide(slide)

        body="""
	<body>
		<div class="reveal">
			<div class="slides">
			    %(titleslide)s
			    %(slides)s
			</div>
		</div>
"""%{'titleslide': title_slide,
     'slides': slides }
     
        return body



    def produce_output(self):
        """ Generates build/index.html."""
        
        header = self.generate_header()
        footer = self.generate_footer()
        body = self.generate_body()
        text = header+body+footer
        with open('index.html', 'w') as outfile:
            outfile.write(text)
    
    def generate_title_slide(self):
    
        authorline="""<br><p>
						"""
        if 'author' in self.meta_info:
            if 'email' in self.meta_info:
                authorline += "<a href=\"mailto:"+str(self.meta_info['email'])+"\" >" + self.meta_info['author'] + "</a>"
            else:
                authorline += self.meta_info['author']
            if 'institution' in self.meta_info:
                authorline += " ("+self.meta_info['institution']+")."
            else:
                authorline += "."
                
        authorline +="""
					</p>"""
                
        dateline="""<br><p>
						"""
        if 'date' in self.meta_info:
            dateline += self.meta_info['date'] + '.'
        dateline+="""
					</p>"""    
        
        code="""
			    <!-- Title slide -->
				<section>
					<h1>%(title)s</h1>
					<h3>%(subtitle)s</h3>
					%(authorline)s
					%(dateline)s
				</section>
""" % {'title': self.meta_info['title'],
       'subtitle': self.meta_info['subtitle'],
       'authorline': authorline,
       'dateline': dateline }
       
        return code   
        
    def generate_slide(self, slide):
        
        slide_content=""
                    
        for content in slide['content']:
            slide_content+=content.html()
                 
        code = """
<!-- Slide -->
<section>
<h2>%(slide_title)s</h2>
%(content)s
</section>
""" % {'slide_title' : slide['title'],
        'content' : slide_content} 

        return code 
