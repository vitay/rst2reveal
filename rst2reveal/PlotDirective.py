import os
from docutils import nodes
from docutils.parsers.rst import directives
try:
    from matplotlib.pylab import *
except:
    pass

def plot_directive(name, arguments, options, content, lineno,
                       content_offset, block_text, state, state_machine):

    # Check if matplotlib is installed
    try:
        import matplotlib.pylab 
    except:
        print 'Warning: matplotlib is not installed on your system. Plots will not be generated.'
        return []
        
    # Process the options
    if 'width' in options.keys():
        width = 'width='+options['width']
    else:
        width = 'width=90%'
    if 'align' in options.keys():
        align = options['align']
    else:
        align = 'center'
#    if align in ['left', 'right']:
#        RevealTranslator.inline_lists = True # how to access this?
    if 'alpha' in options.keys():
        alpha = options['alpha']
    else:
        alpha = '1.0'
    try:
        alpha = float(alpha)
        if alpha <0.0:
            alpha = 0.0
        elif alpha > 1.0:
            alpha = 1.0
    except:
        print 'Error: alpha must be a floating value between 0.0 and 1.0'
        return []
    if 'invert' in options.keys():
        import matplotlib
        matplotlib.rcParams['figure.facecolor'] = 'b'
        matplotlib.rcParams['figure.edgecolor'] = 'b'
        matplotlib.rcParams['text.color'] = 'w'
        matplotlib.rcParams['axes.edgecolor'] = 'w'
        matplotlib.rcParams['axes.labelcolor'] = 'w'
        matplotlib.rcParams['xtick.color'] = 'w'
        matplotlib.rcParams['ytick.color'] = 'w'
        matplotlib.rcParams['legend.frameon'] = False
        if not 'alpha' in options.keys(): # not specified, so default = 0.0
            alpha = 0.0
    
    
    # Execute the code... RISKY!
    try:
        fig = figure()
        for line in content:
            exec(line)
        fig.patch.set_alpha(alpha)
        for ax in fig.axes:
            ax.patch.set_alpha(alpha)
        fig.savefig('__temp.svg', dpi=600, edgecolor='w')
    except Exception, e:
        print 'Error while generating the figure:'
        for line in content:
            print '    ', line
        print e
        return []

        
    # Extract the generated data
    start = False
    text = "<div class=\"align-%(align)s\">\n" % {'align': align}
    with open('__temp.svg', 'r') as infile:
        for aline in infile:
            if aline.find('<svg ') != -1:
                start = True
                text += '   <svg class=\"align-%(align)s\" %(width)s viewBox="0 0 576 432" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg >"\n' % {'align': align, 'width': width}
            elif start:
                text += '   ' + aline 
    text += "\n</div>\n"
    os.system('rm -f __temp.svg')
        
    return [nodes.raw('matplotlib', text, format='html')]

plot_directive.content = 1
plot_directive.arguments = (0, 0, 0)
plot_directive.options = {'align': directives.unchanged, 'width': directives.unchanged, 'alpha': directives.unchanged, 'invert': directives.unchanged}

directives.register_directive('matplotlib', plot_directive)
