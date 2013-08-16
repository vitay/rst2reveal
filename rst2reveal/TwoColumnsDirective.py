""" Two-columns directive.

Usage:

.. column:: left

    * item
    
    * item
    
.. column:: right

    * item
    
    * item 
"""

# Define the nodes.
from docutils import nodes
from RevealTranslator import RST2RevealTranslator

class LeftColumnNode(nodes.Part, nodes.Element): pass
class RightColumnNode(nodes.Part, nodes.Element): pass 

def visit_left_column(self, node):
    self.body.append(' '*12 + '<div class="columns"><div class="left">\n')

def depart_left_column(self, node):
    self.body.append(' '*12 + '</div>\n')
            
def visit_right_column(self, node):
    self.body.append(' '*12 + '<div class="right">\n')

def depart_right_column(self, node):
    self.body.append(' '*12 + '</div></div>\n')

def add_node(node, **kwds):
    nodes._add_node_class_names([node.__name__])
    for key, val in kwds.iteritems():
        try:
            visit, depart = val
        except ValueError:
            raise ExtensionError('Value for key %r must be a '
                                 '(visit, depart) function tuple' % key)

        assert key == 'html', 'accept html only'

        setattr(RST2RevealTranslator, 'visit_'+node.__name__, visit)
        setattr(RST2RevealTranslator, 'depart_'+node.__name__, depart)
            

add_node(LeftColumnNode, html=(visit_left_column, depart_left_column))
add_node(RightColumnNode, html=(visit_right_column, depart_right_column))

# Define the Directive
from docutils.parsers.rst import Directive

class Column(Directive):

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    has_content = True

    node_class = None

    def run(self):
        # Raise an error if the directive does not have contents.
        self.assert_has_content()
        text = '\n'.join(self.content)
        # Left or right column?
        if self.arguments[0] in ['left', 'Left']:
            self.node_class = LeftColumnNode
        if self.arguments[0] in ['right', 'Right']:
            self.node_class = RightColumnNode
        # Create the admonition node, to be populated by `nested_parse`.
        column_node = self.node_class(rawsource=text)
        # Parse the directive contents.
        self.state.nested_parse(self.content, self.content_offset,
                                column_node)
        return [column_node]    
               
                 
                 
from docutils.parsers.rst import directives
directives.register_directive('column', Column)         

