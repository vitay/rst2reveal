from RSTParser import *

class Text:

    def __init__(self, el):
        self.el = el
        
    def html(self):
        if type(self.el) == type(""):
            return self.el
        return self.el.text
        
class Emphasis:

    def __init__(self, el):
        self.el = el
        
    def html(self):
        return '<em>' + self.el.text + '</em>'
        
class Strong:

    def __init__(self, el):
        self.el = el
        
    def html(self):
        return '<strong>' + self.el.text + '</strong>'
        
class Literal:

    def __init__(self, el):
        self.el = el
        
    def html(self):
        return '<code>' + self.el.text + '</code>'
        
class Reference:

    def __init__(self, el):
        self.el = el
        
    def html(self):
        [(tmp, url), (tmp, name)]=self.el.items()
        return '<a  href=\"' + url + '\">' + name + '</a>'

class Paragraph:
    """ Represents a paragraph. """

    def __init__(self, el):    
        self.el = el
        self.parts = []
        special =[item for item in self.el.iter()]
        for text in self.el.itertext():
            found=False
            for item in special:
                if text == item.text: # not a normal text
                    if item.tag == "paragraph":
                        self.parts.append(Text(item))
                    elif item.tag == "emphasis":
                        self.parts.append(Emphasis(item))
                    elif item.tag == "strong":
                        self.parts.append(Strong(item))
                    elif item.tag == "literal":
                        self.parts.append(Literal(item))
                    elif item.tag == "reference":
                        self.parts.append(Reference(item))
                    elif item.tag == "target":
                        pass
                    special.remove(item)
                    found=True
                    break
            if not found: # Plain text
                self.parts.append(Text(text))
                
       
    def html(self):
        code =  "<p> " 
        for part in self.parts:
            code+= part.html() 
        code += "</p>"
        return code
        
class List:

    def __init__(self, el):
    
        self.items=[]
        
        for child in el: # list_items, have only one child
            for child2 in child: # Should be a paragraph
                self.items.append(Paragraph(child2))
                
    def html(self):
        code_items=""
        for item in self.items:
            code_items += "<li> " + item.html() + '\n'
    
        code= """
<ul>
%(items)s
</ul>
""" % {'items': code_items}

        return code
        
class EnumeratedList:

    def __init__(self, el):
    
        self.items=[]
        
        for child in el: # list_items, have only one child
            for child2 in child: # Should be a paragraph
                self.items.append(Paragraph(child2))
                
    def html(self):
        code_items=""
        for item in self.items:
            code_items += "<li> " + item.html() + '\n'
    
        code= """
<ol>
%(items)s
</ol>
""" % {'items': code_items}

        return code
        
class Code:

    def __init__(self, el):
    
        self.el = el
                
    def html(self):
    
        code_content=self.el.text
        code= """
<pre><code data-trim contenteditable>
%(code)s
</code></pre>
""" % {'code': code_content}

        return code
