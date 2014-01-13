"""vspace role. Used to add vertical space before an element as multiple of one line height.

:vspace:`2`
"""


# Define the role
from docutils.parsers.rst import roles
from docutils import nodes

def vspace_role(role, rawtext, text, lineno, inliner,
                       options={}, content=[]):

    try:
        nb_lines = int(text)
    except:
        print 'Error in', rawtext, ': argument should be an integer.'
        nb_lines=0
    node = nodes.raw('', '<br>'*nb_lines, format='html')
    return [node], []

roles.register_local_role('vspace', vspace_role)
