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
        print('Warning: matplotlib is not installed on your system. Plots will not be generated.')
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
        alpha = '0.0'
    try:
        alpha = float(alpha)
        if alpha <0.0:
            alpha = 0.0
        elif alpha > 1.0:
            alpha = 1.0
    except:
        print('Error: alpha must be a floating value between 0.0 and 1.0')
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
    
    
    # Execute the code line by line
    try:
        fig = figure()
        for line in content:
            exec(line)
        # Set transparency
        fig.patch.set_alpha(alpha)
        for ax in fig.axes:
            ax.patch.set_alpha(alpha)
#            if ax.get_legend() is not None:
#                for child in ax.get_legend().get_children():
#                    child.set_alpha(alpha)
        # Call XKCDify
        if 'xkcd' in options.keys():
            if options['xkcd'] != '':
                try:
                    mag = float(options['xkcd'])
                except:
                    print('Error: the argument to :xkcd: must be a float.')
                    return []
            else:
                mag=1.5
            from XKCDify import XKCDify
            for ax in fig.axes:
                XKCDify(ax, mag=mag, 
                        bgcolor = 'k' if 'invert' in options.keys() else 'w',
                        forecolor = 'w' if 'invert' in options.keys() else 'k',
                        xaxis_arrow='+', yaxis_arrow='+',
                        ax_extend= 0.05,
                        expand_axes=(len(fig.axes) == 1))
        # Save the figure in a temporary SVG file
        fig.savefig('__temp.svg', dpi=600, edgecolor='w')
        # Optionally save the figure
        if 'save' in options.keys():
            fig.savefig(options['save'], dpi=600)
        
    except Exception as e:
        print('Error while generating the figure:')
        for line in content:
            print('    ', line)
        print(e)
        return []

        
    # Extract the generated data
    start = False
    text = "<div class=\"align-%(align)s\">\n" % {'align': align}
    with open('__temp.svg', 'rb') as infile:
        for aline in infile:
            if aline.find('<svg ') != -1:
                start = True
                text += '   <svg class=\"align-%(align)s\" %(width)s viewBox="0 0 576 432" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg >"\n' % {'align': align, 'width': width}
            elif start:
                try:
                    text += '   ' + unicode(aline) 
                except: 
                    pass
    text += "\n</div>\n"
    os.system('rm -f __temp.svg')
        
    return [nodes.raw('matplotlib', text, format='html')]

plot_directive.content = 1
plot_directive.arguments = (0, 0, 0)
plot_directive.options = {'align': directives.unchanged, 'width': directives.unchanged, 'alpha': directives.unchanged, 'invert': directives.unchanged, 'xkcd': directives.unchanged, 'save': directives.unchanged}

directives.register_directive('matplotlib', plot_directive)
