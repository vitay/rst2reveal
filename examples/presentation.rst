==========
rst2reveal
==========

ReST to Reveal.js translator
++++++++++++++++++++++++++++

:author: Julien Vitay
:date: August 2013
:email: julien.vitay@gmail.com


ReST to Reveal.js translator
============================

* **rst2reveal** is intended to transform regular reStructuredText (ReST) text files to HTML5 slides using some features of the `Reveal.js <http://revealjs.com/>`_ Javascript library developped by `Hakim El Hattab <http://hakim.se>`_. 

* It aims at providing a quick and easy way to produce nice and consistent HTML slides for teaching or scientific use, not fancy presentations. 

* **Reveal.js** has more features than what **rst2reveal** can produce, so if you are more fluent in HTML than ReST, you should use it directly. 

* **rst2reveal** ships some parts of Reveal.js (mainly ``.js`` and ``.css`` files), so it is released under the same MIT license.


Basic ReST markup
=================


Basic ReST markup
=================

**rst2reveal** processes the usual ReST inline markup:

* **Bold** : ``**Bold**``

* *Italic* : ``*Italic*``

* ``Literals`` : ````Literals````

* Subscripts H\ :sub:`2`\ O and supscripts E = mc\ :sup:`2` : 

    ``H\ :sub:`2`\ O and E = mc\ :sup:`2```

* `Links <http://www.example.com>`_ : ```Links <http://www.example.com>`_``


Lists
=====

**Bulleted lists**

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

:: 

    * This is a bulleted list.
    * It has two items, the second
      item uses two lines.

**Enumerated lists**

1. This is a numbered list.
2. It has two items too.

::

    1. This is a numbered list.
    2. It has two items too.

Structure of a ReST document
============================

The input file should have a hierarchical structure, with the different sections underlined (optionally also overlined) by special characters::

    #########################
    Title of the presentation
    #########################
    
    Subtitle
    ++++++++
    
    :author: Me
    :date: now
    
    Title of the first slide
    ========================
    
    * Content of the ...
    
    * ... first slide
    
    Title of the second slide
    =========================
    
    * Content of the ...
    
    * ... second slide


Structure of a ReST document
============================

The choice of the marker characters is free. The line must be at least as long as the text.

* The first level header defines the title of the presentation::

    #########################
    Title of the presentation
    #########################

* The second level (if any) defines the subtitle of the presentation::

    Subtitle
    ++++++++

* The third level defines the title of each slide::
    
    Title of the first slide
    ========================
    

    
Subslides
=========

* Optionally, fourth-level headers define subslides in Reveal.js

* They are accessed by pressing the up and down keys, as opposed as the left/right keys for normal slides::

    First subslide
    --------------

    Content of the first subslide.

    Second subslide
    ---------------

    Content of the second subslide.

* It is useful for a finer structuring of your presentation, or when planning additional slides if the audience has questions (instead of dumping them at the end).

First subslide
--------------

Content of the first subslide.

Second subslide
---------------

Content of the second subslide.

Field lists
===========

It is possible to define *field lists* at the beginning of the document to generate the metadata used for the generation of the first slide and of the footer::

    #########################
    Title of the presentation
    #########################
    
    Subtitle
    ++++++++
    
    :author: Me
    :date: now
    :institution: My university
    :email: me@example.com
    
It is possible to add other fields than these four, but the template for the first slide will need to be adapted.

Directives processed by rst2reveal
==================================

Directives processed by rst2reveal
==================================

* For a richer content than these basic markups, you'll need to use the docutils **directives**.

* Some of the standard directives are processed by rst2reveal:

    * math
    * topic, sidebar
    * admonitions (note, warning)
    * code-block
    * image
    * epigraph
    * raw
    * include
    
* Other may not be styled yet (but it can be extended) or do not make sense in this context (a table of content would display all slide titles).

Directives processed by rst2reveal
==================================

* **rst2reveal** additionally implements several custom directives particularly suited for scientific presentations:

    * video
    * matplotlib
    * columns
    
* However, usage of these directives disrupts the compatibility of your input file with other ReST renderers (Sphinx, pandoc...).

Usual directives
================

Displaying mathematical equations
=================================

Mathematical terms can be rendered inline :math:`x(t)` using `MathJax.js <http://www.mathjax.org/>`_::

    :math:`x(t)`

Equations can also be displayed as blocks:

.. math::

    \tau \frac{dx(t)}{dt} + x(t) = f(t)

::

    .. math::

        \tau \frac{dx(t)}{dt} + x(t) = f(t)
    
It also understands the LaTeX ``align*`` mode:

.. math::

    a &= b + c \\
    b &= a + d

::

    .. math::

        a &= b + c \\
        b &= a + d
    
Images
======


.. image:: http://collider.com/wp-content/uploads/monty-python-image-600x450.jpg
    :width: 40%
    :align: center
    
    
* Images can be centered and scaled between 0 and 100% using the ``image`` directive::
       
    .. image:: http://collider.com/wp-content/uploads/monty-python-image-600x450.jpg
        :width: 40%
        :align: center
        
* You can provide either an URL or a path relative to the current directory.   

Images
======

.. image:: http://collider.com/wp-content/uploads/monty-python-image-600x450.jpg
    :width: 50%
    :align: right
    
* Images can also be aligned to the left or to the right, with the corresponding scaling:
       
``:width: 50%``

``:align: right``

Code blocks
===========

The default way to show some code is to end a line with ``::`` and indent the code::

    from rst2reveal import Parser
    parser = Parser( input_file='index.rst', 
                     output_file='index.html',
                     theme='beige' )                          
    parser.create_slides()
    
Like this::  

    The default way to show some code is to end a line with ``::`` and indent the code::

        from rst2reveal import RSTParser
        parser = RSTParser(  input_file='index.rst', 
                             output_file='index.html',
                             theme='beige' )                          
        parser.create_slides()  
        

Code blocks
===========

* If you want to color-highlight the code, you need to have the Python package `Pygments <http://www.pygments.org>`_ installed on your computer. 

* You can then use the ``code-block`` directive by specifying the language as an argument: 

.. code-block:: python

    from rst2reveal import Parser
    parser = Parser( input_file='index.rst', 
                     output_file='index.html',
                     theme='beige' )                          
    parser.create_slides()
    
Like this::

    .. code-block:: python

        from rst2reveal import Parser
        parser = Parser( input_file='index.rst', 
                         output_file='index.html',
                         theme='beige' )                          
        parser.create_slides()
    

Code blocks
===========    
    
`Pygments <http://www.pygments.org>`_ can highlight a lot of languages, for example C++:

.. code-block:: c++

    #include <stdio>
    
    void test() {    
        for(int i=0; i<10; i++) {
            sleep(1);
        }
    
        std::cout << "Hello, World!" << std::endl;
    }
    
::

    .. code-block:: c++

        #include <stdio>
        
        void test() {    
            for(int i=0; i<10; i++) {
                sleep(1);
            }
        
            std::cout << "Hello, World!" << std::endl;
        }
    
Code blocks
===========  

* There is a big selection of themes you can use to highlight the code, by specifying the ``pygments_style`` option to rst2reveal (depending on your Pygments version)

    :small:`monokai, manni, perldoc, borland, colorful, default, murphy, vs, trac, tango, fruity, autumn, bw, emacs, vim, pastie, friendly, native`

* Especially if you use a dark theme, it is advised to change the Pygments style (to monokai or manni for example).

* You can specify the ``:linenos:`` option to the ``code-block`` directive to add line numbers.
    
.. code-block:: c++
    :linenos:

    #include <stdio>
    
    void test() {    
        for(int i=0; i<10; i++) {
            sleep(1);
        }
    
        std::cout << "Hello, World!" << std::endl;
    }
    
Topic
=====

The ``topic`` directive allows to highlight important blocks of text with a title:

.. topic:: Equation

    A leaky integrator is defined by:
    
    .. math::

        \tau \frac{dx(t)}{dt} + x(t) = f(t)

Source::

    .. topic:: Equation

        A leaky integrator is defined by:
        
        .. math::

            \tau \frac{dx(t)}{dt} + x(t) = f(t)

Admonitions
===========
    
Admonitions are similar to topic, but the title is built-in. For now, only ``note``:    
    
.. note:: 

    This is a note  

:: 

    .. note:: 

        This is a note   
    
and ``caution`` are implemented:   
    
.. caution::

    This is a warning  
    
::

    .. caution::

        This is a warning     
 

Sidebar
=======

.. sidebar:: Sidebar Title
   :subtitle: Optional Sidebar Subtitle
   :class: right

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.
   
* Sidebars are topics covering only 50% of the screen, floating either on the left or right side of the slide.

* They optionally take subtitles.

* Position is determined by the ``class`` attribute.

:: 

    .. sidebar:: Sidebar Title
       :subtitle: Optional Sidebar Subtitle
       :class: right

       Subsequent indented lines comprise
       the body of the sidebar, and are
       interpreted as body elements.
    
    

Sidebar
=======


.. sidebar:: An image
    :subtitle: with its subtitle
    :class: left

    .. image:: http://collider.com/wp-content/uploads/monty-python-image-600x450.jpg
        :width: 100%
        
    :small:`Fig. 1: legend of the image.`
   
   
* Sidebars can be useful to provide a title and legend to an image.

* The legend can be made smaller by using the ``small`` role:

    ``:small:`Fig. 1: legend of the image.```
    
 
Raw HTML
========

* In case rst2reveal does not offer what you need and you want to generate some HTML code by yourself, you can use the ``raw:: html`` directive, which will simply dump the content of the directive into the generated code::

    .. raw:: html

        <span style="color:#ff0000">Some text in red!</span>

.. raw:: html

    <span style="color:#ff0000">Some text in red!</span>


Citations
=========

Citations can be rendered with the role ``epigraph``:

.. epigraph::

    "L'important, c'est de bien s'ennuyer."
    
    -- Jean Carmet
    
::

    .. epigraph::

        "L'important, c'est de bien s'ennuyer."
        
        -- Jean Carmet
     
 
Directives specific to rst2reveal
=================================    
    
Videos
======


.. video:: http://techslides.com/demos/sample-videos/small.ogv
    :width: 70%

* Videos can displayed with the HTML5 video tag   

::
    
    .. video:: http://techslides.com/demos/sample-videos/small.ogv
        :width: 70%
        
Videos
======


.. video:: http://techslides.com/demos/sample-videos/small.ogv
    :width: 30%

* You can specify the ``loop`` and ``autoplay`` options to the directive to loop the video or start the video as soon as the slide appears.

::
    
    .. video:: http://techslides.com/demos/sample-videos/small.ogv
        :width: 70%
        :loop:
        :autoplay:
        
* The video must be in ``.webm``, ``.ogv`` or ``.mp4`` depending on your browser. Other formats can not be played.
        

    
Incremental display
===================

You can incrementally display the content of your slide by using the ``fragment`` class:

.. class:: fragment

    ::
    
        .. class:: fragment

            * Items will be displayed in the order of their declaration.

            * It applies until the end of the slides.

    * Items will be displayed in the order of their declaration.

    * It applies until the end of the current slide.


            
Matplotlib
==========

You can directly generate plots if matplotlib is installed:

.. matplotlib:: 
    :align: center
    :width: 70%
    
    import numpy as np
    ax = axes()
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x) * np.exp(-0.1 * (x - 5) ** 2), 'b', lw=3, label='damped sine')
    ax.plot(x, -np.cos(x) * np.exp(-0.1 * (x - 5) ** 2), 'r', lw=3, label='damped cosine')
    ax.set_title('check it out!')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.legend(loc='upper right')
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.0, 1.0)
            
Matplotlib
==========

Simply use the ``matplotlib`` directive and write the corresponding matplotlib code:

.. code-block:: python

    .. matplotlib:: 
        :align: center
        :width: 80%
        
        import numpy as np
        ax = axes()
        x = np.linspace(0, 10, 100)
        ax.plot(x, np.sin(x) * np.exp(-0.1*(x-5)**2), 'b', 
                lw=3, label='damped sine')
        ax.plot(x, -np.cos(x) * np.exp(-0.1*(x-5)**2), 'r', 
                lw=3, label='damped cosine')
        ax.set_title('check it out!')
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')
        ax.legend(loc='upper right')
        ax.set_xlim(0, 10)
        ax.set_ylim(-1.0, 1.0)
    
Matplotlib
==========

* You basically only need to write everything you would normally put between:

.. code-block:: python

    from pylab import *
    fig = figure()
    
and:

.. code-block:: python

    show()
    
* The python code is interpreted "as-if" with ``exec`` statements, so be careful with what you write!

* The figure is internally generated in ``.svg`` format, and pasted in the HTML source.
 
Matplotlib
========== 
 
* If you use a dark background, you can either:

    * control the transparency of the figure background with the ``:alpha:`` option (between 0.0 and 1.0).
    
    * invert all colours and use a transparent background with the ``:invert:`` option.
 
Matplotlib
========== 

* By providing the ``:xkcd:`` option, you can alter the rendering of the plot to give it a hand-drawn look-and-feel.

* You can optionally provide a float as an option to :xkcd: to define the amount of distortion (0.0 = None, 1.5 = default).  

* The function is based on the script provided by `Jake Vanderplas <http://jakevdp.github.io/blog/2012/10/07/xkcd-style-plots-in-matplotlib/>`_.

* If you use Matplotlib 1.3, you now just need to call ``xkcd()`` in your code.
 
 
.. matplotlib:: 
    :align: center
    :width: 50%
    :xkcd:
    
    import numpy as np
    ax = axes()
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x) * np.exp(-0.1 * (x - 5) ** 2), 'b', lw=3, label='damped sine')
    ax.plot(x, -np.cos(x) * np.exp(-0.1 * (x - 5) ** 2), 'r', lw=3, label='damped cosine')
    ax.set_title('check it out!')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.legend(loc='upper right')
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.0, 1.0) 
 
Two columns
===========


.. column:: left

    .. matplotlib:: 
        :align: center
        :width: 100%
        :xkcd:
        
        import numpy as np
        ax = axes()

        x = np.linspace(0, 10, 100)
        ax.plot(x, np.sin(x) * np.exp(-0.1 * (x - 5) ** 2), 'b', lw=3, label='damped sine')
        ax.plot(x, -np.cos(x) * np.exp(-0.1 * (x - 5) ** 2), 'r', lw=3, label='damped cosine')

        ax.set_title('check it out!')
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')

        ax.legend(loc='upper right')

        ax.set_xlim(0, 10)
        ax.set_ylim(-1.0, 1.0)
        
    * Some text describing the plot.
            
        
.. column:: right

    
    * You can also use a two-columns environment (of the same size), if the default floating behaviour around images, videos, etc. does not suit your needs.
    
    * You simply need to call twice the ``column`` directive, once with the "left" argument, and once with "right" (in that order, otherwise it fails)::


        .. column:: left
        
            * Content in the left column

        .. column:: right
        
            * Content in the right column
            
            
Configuring rst2reveal
======================

Configuring rst2reveal
======================

* **rst2reveal** can be used as a script after installation::

    rst2reveal presentation.rst
    
* This creates a ``reveal/`` subfolder containing the Javascript and CSS code, and generates ``presentation.html`` which can then be rendered in your browser.

* You can also call it from Python: ``help(rst2reveal.Parser)`` 

.. code-block:: python

    from rst2reveal import Parser
    parser = Parser( input_file='index.rst', 
                     output_file='index.html',
                     theme='beige' )                          
    parser.create_slides()

Configuring rst2reveal
======================

**rst2reveal** has plenty of options allowing to fine-tune your presentation (type ``rst2reveal -h``):

* Horizontal and vertical alignment of the titles and slide content.

* The CSS theme (currently to be chosen between "default", "beige" and "night")

* The Javascript transition between the slides.

* The presence of a footer and slide numbers below the slides.

Defining your own theme
=======================

* To define your own CSS theme, you just need to inherit from the default theme, found at::
    
    ./reveal/css/theme/default.css
    
and modify the CSS properties that you need.

* You can then specify this new theme with the argument::

    rst2reveal presentation.rst --stylesheet custom.css
    
* You can also use both a basic theme and a slight modification in your own CSS file.

Using a configuration file
==========================

* To avoid re-typing all the arguments to ``rst2reveal``, you can also generate a configuration file with::

    rst2reveal --generate_configuration presentation.conf
    
* Once adapted to your needs, you only need to call::

    rst2reveal presentation.conf 
    
to compile the ReST file with the desired options.

* The configuration file must end with ``.conf``, ``.cfg`` or ``.ini``.

