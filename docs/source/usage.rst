Usage
=====

.. _installation:

Dependencies
------------
Before launching the **REST** package, please ensure following dependencies are met by the system:
   1. *Java-11 (SDK)*.
   2. *gfortran*.
   3. *xterm*
   4. *Python3*
   5. *Visualization-Tool-Kit (VTK)*
   6. *PyVista-0.29.0*
   
.. warning::
   There are some issues in current versions of PyVista due to which it may not be able to plot the .VTK files. Please install *PyVista* version - 0.29.0 or lower than that. Avoid installing recent verions of *PyVista*.


Installation
------------
**REST** is very easy to install and run over a linux system or wslg.

1. Download the REST.zip file from the link.
2. Unzip the package and enter the **REST** directory.
3. Open the terminal in the **REST** directory and type the following command to launch the **REST** *GUI*:

.. code-block:: console

       $./REST.sh

First Run
---------




To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

