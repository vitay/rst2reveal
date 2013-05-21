#!/usr/bin/env python
try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

import sys
import os
import docutils
from docutils.frontend import OptionParser
from docutils.utils import new_document
from docutils.parsers.rst import Parser
import xml.etree.ElementTree as ET

from HTMLWriter import HTMLWriter
import Directives

class RSTParser:
    
    def __init__(self, input_file='index.rst', theme='custom-beige', transition = 'fade'):
    
        self.input_file = input_file
        self.theme = theme # default, beige, sky, night, serif, simple, solarized, moon, custom-night
        self.transition = transition # default/cube/page/concave/zoom/linear/fade/none

    def extract_meta(self):
        """ Extracts meta-info."""
        self.meta_info={  'title': 'Presentation', 'subtitle': '' } # Default
                       
        for child in self.tree:
            if child.tag == 'title':
                self.meta_info['title'] = child.text
            if child.tag == 'field_list': # list of fields
                for field in child:
                    field_name = self.process_text_element(field.find('field_name'))
                    field_value = self.process_text_element(field.find('field_body/paragraph'))
                    self.meta_info[field_name] = field_value
                
                
    def process_text_element(self, el):
        """ Processes an element until some text is found (e.g. email for the title slide). """
    
        if el.text == None: # Not a text yet, must follow the hierarchy
            parent = el
            text = None
            while text == None:
                for child in parent:
                    if child.text != None:
                        return child.text
                    else:
                        parent =child
        else:
            return el.text
        
    def process_slide(self, slide):
        """ Recursively examines the content of a slide."""
        
        slide_content={'title': '', 'content': []}
        for child in slide:
            if child.tag == 'title':
                slide_content['title'] = child.text
            elif child.tag == 'bullet_list': # bullet list
                slide_content['content'].append(Directives.List(child))
            elif child.tag == 'enumerated_list': # enumerated list
                slide_content['content'].append(Directives.EnumeratedList(child))
            elif child.tag == 'paragraph': # single paragraph
                slide_content['content'].append(Directives.Paragraph(child))
            elif child.tag == 'literal_block': # code sample
                slide_content['content'].append(Directives.Code(child))
                
        return slide_content
        

    def create_slides(self):

        # Parse the file using docutils:
        settings = OptionParser(components=(Parser,)).get_default_values()
        parser = Parser()
        document = new_document(self.input_file, settings)
        with open(self.input_file) as infile:
            parser.parse(infile.read(), document)
        print document
        
        # Read the tree
        self.tree=ET.fromstring(str(document))[0]
        self.extract_meta()
        self.structure = {'meta_info': self.meta_info, 'slides': [] }  
        for child in self.tree:
            if child.tag == 'section':
                self.structure['slides'].append(self.process_slide(child))
            else: # Something else to write on the first page
                pass
                
        # Produce output
        print self.structure
        self.producer = HTMLWriter(self)
        self.producer.produce_output()
        

if __name__ == '__main__':
    # Create the object
    parser = RSTParser()
    # Create the slides
    parser.create_slides()
