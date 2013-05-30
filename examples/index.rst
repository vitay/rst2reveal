==============================
rst2reveal
==============================

:subtitle: ReST to Reveal.js translator
:author: Julien Vitay
:institution: TU Chemnitz
:date: May 2013
:email: julien.vitay@informatik.tu-chemnitz.de



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

.. math::

    \tau \frac{dx}{dt} + x = a
    
Code?
===========

In Python:

.. code-block:: python

    import numpy as np
    np.ones((10, 10))
    res = a + b
    
In C++:

.. code-block:: c++

    void test(){
        int i = 0;
        for(int i=0; i<10; i++){
            sleep(1);
        }
        std::cout << "Hello, World!" << std::endl;
    }
    
Images
==============

.. image:: amygdala.jpg
    :width: 50%
    :align: right
    

* Images can be centered and scaled between 0 and 100%

* Aligned to the left 

* or to the right...

Images
==============

.. image:: drawing.svg
    :width: 100%
    :align: center
    

SVG too.



    
Videos?
==============


.. video:: matthews.webm
    :width: 50%
    :autoplay:
    
* A video explaining the Active Appearance Model.

* Matthews  
    
Raw HTML
================

.. raw:: html

    <b> Some text </b>
    
Admonitions
==========================
    
.. note::

    This is a note    
    
Are there subsections?
==========================

Yes, go down!

This one
++++++++++++++++

is a subsection

This one
++++++++++++++++

is another



And you go back to the previous level
=============================================

Citations are with the role ``epigraph``:

.. epigraph::

    L'important, c'est de bien s'ennuyer.
    
    -- Jean Carmet
    
Incremental reveal
========================

.. class:: fragment

    * First item

    * Second item
    
        * Nested too?
        
        * Let's see
    
    Some text
