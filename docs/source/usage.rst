Usage
=====

.. _installation:

Installation
------------
**REST** is very easy to install and run over a linux system or wslg.
   1. Download the REST.zip file from the link.
   2. Unzip the package and enter the **REST** directory.
   3. Open the terminal in the **REST** directory and type the following command to start the **REST** *GUI*:
      
.. code-block:: console
    $./REST.sh


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

