from docutils import nodes
from docutils.parsers.rst import directives

CODE = """\
    <div class="align-%(align)s">
    <video style="text-align:%(align)s; float:%(align)s" width="%(width)s" %(autoplay)s %(loop)s controls>
      <source src="%(filename)s" type="video/webm">
      Your browser does not support the video tag.
    </video>
    </div>
"""


def video(name, args, options, content, lineno,
            contentOffset, blockText, state, stateMachine):
    """ Restructured text extension for inserting videos """
    if len(content) == 0:
        return
    string_vars = {
        'filename': content[0],
        'width': '50%',
        'align': 'center',
        'autoplay': '',
        'loop': ''
        }
    extra_args = content[1:] # Because content[0] is ID
    args={}
    import re
    for ea in extra_args:
        name = re.findall(r':(.+):', ea)[0]
        if len(re.findall(name+r':(.+)', ea))>0:
            value = re.findall(name+r':(.+)', ea)[0]
        else:
            value=''
        args[name] = value
    if 'width' in args.keys():
        string_vars['width'] = args['width'].strip()
    if 'align' in args.keys():
        string_vars['align'] = args['align'].strip()
    if 'autoplay' in args.keys():
        string_vars['autoplay'] = 'autoplay'
    if 'loop' in args.keys():
        string_vars['loop'] = 'loop'
        
    return [nodes.raw('video', CODE % (string_vars), format='html')]
    
video.content = True
directives.register_directive('video', video)
