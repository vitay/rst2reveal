==================================
rst2reveal
==================================

ReST to Reveal.js translator
--------------------------------------

:author: Julien Vitay
:date: August 2013
:email: julien.vitay@gmail.com



Bullet lists
============================

* A first *nested* **list** with ``verbatim code``

* Very `interesting <http://www.google.fr>`_, but if the line is very long what happens? Something special?

    * Also works with nested lists.
    
    * What happens if the line is really really long, does the bullet point go to far away? 


With an additional paragraph...

Enumerated lists
============================


1. An **enumerated** list with a very long line, let's see what happens.

2. Very :strong:`interesting`

Another slide
===================

1- Let's test ``verbatim``

2- And `URLs <http://www.google.fr>`_

What about math?
===================

Inline :math:`x(t)`

Equation:

.. math::

    \tau \frac{dx}{dt} + x = a
    
Also with ``align*`` mode:

.. math::

    a &= b +c \\
    b &= a + 10
    
Code
===========

The Pygments package can very easily highlight Python code using different patterns:

.. code-block:: python

    import numpy as np
    
    a = np.ones((10, 10))
    
    b = np.ones((10, 10))
    
    res = a + b
    
This is true for a lot of languages, including C++:

.. code-block:: c++

    void test()
    {
    
        int i = 0;
    
        for(i=0; i<10; i++)
        {
            sleep(1);
        }
    
        std::cout << "Hello, World!" << std::endl;
    }
    
There is a huge selection of themes you can use to highlight the code.
 
    
Images
==============

.. image:: http://collider.com/wp-content/uploads/monty-python-image-600x450.jpg
    :width: 50%
    :align: right
    

* Images can be centered and scaled between 0 and 100%

* Aligned to the left or to the right...

Images
==============

.. image:: http://collider.com/wp-content/uploads/monty-python-image-600x450.jpg
    :width: 90%
    :align: center
    
       
Videos
==============


.. video:: http://techslides.com/demos/sample-videos/small.ogv
    :width: 70%
    :align: center

* Videos can displayed with the HTML5 video tag   

::
    
    .. video:: http://techslides.com/demos/sample-videos/small.ogv
        :width: 70%
        :align: center
        
Raw HTML
================

.. raw:: html

    <b> Some text </b>
    
::

    .. raw:: html

        <b> Some text </b>
    
Admonitions
==========================
    
You can use admonitions, such as note:    
    
.. note:: 

    This is a note   
    
Warning or caution   
    
.. caution::

    This is a warning
      
    

    
Are there subsections?
==========================

This one
++++++++++++++++

is a subsection

This one
++++++++++++++++

is another



And you go back to the previous level and look at very long titles
========================================================================

Citations are with the role ``epigraph``:

.. epigraph::

    "L'important, c'est de bien s'ennuyer."
    
    -- Jean Carmet
    
Incremental reveal
========================

.. class:: fragment

    * First item

    * Second item


    ::
    
        .. class:: fragment

            * First item

            * Second item
            
Test svg
============

You can directly plot with matplotlib:

.. matplotlib:: 
    :align: center
    :width: 80%
    :invert:
    
    import numpy as np
    ax = axes()

    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x) * np.exp(-0.1 * (x - 5) ** 2), 'b', lw=3, label='damped sine')
    ax.plot(x, -np.cos(x) * np.exp(-0.1 * (x - 5) ** 2), 'r', lw=3, label='damped cosine')

    ax.set_title('check it out!')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')

    ax.legend(loc='lower right')

    ax.set_xlim(0, 10)
    ax.set_ylim(-1.0, 1.0)
            
Test svg
============

.. matplotlib:: 
    :align: center
    :invert:


    import numpy as np
    x = linspace(1, 100, 100)
    y = x**2
    z = np.sqrt(x)
    ax = subplot(121)
    ax.plot(x, y, linewidth=3)
    ax = subplot(122)
    ax.plot(x, z, linewidth=3)
    
 
    
Images
==============

.. image:: http://collider.com/wp-content/uploads/monty-python-image-600x450.jpg
    :width: 50%
    :align: right
    

* Images can be centered and scaled between 0 and 100%

* Aligned to the left or to the right...
