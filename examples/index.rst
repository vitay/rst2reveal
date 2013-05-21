==============================
Subbacultcha
==============================

:subtitle: ReST to Reveal.js translator
:author: Julien Vitay
:institution: TU Chemnitz
:date: May 2013
:email: julien.vitay@informatik.tu-chemnitz.de


Bullet lists
============================

* A first *nested* **list** with ``verbatim code``

* Very `interesting <http://www.google.fr>`_

With an additional paragraph...

Enumerated lists
============================

1. An **enumerated** list

2. Very interesting

Code highlighting
========================

Here is some sample Python code:

.. code-block::

    import numpy as np
    a = np.ones( (10, 10) )
    b = 2. * np.ones( (10, 10) )
    
    c = a.*b

and here some **C++** code:

.. code-block:: 

    include <stdio>

    int main(){
    
        cout " Hello, World! endl;
    }
