"""small role.

:small:`text`
"""


# Define the role
from docutils.parsers.rst import roles
from docutils import nodes

def small_role(role, rawtext, text, lineno, inliner,
                       options={}, content=[]):

    node = nodes.inline(rawtext, text, **options)
    node['classes']=['small']
    return [node], []

roles.register_local_role('small', small_role)
