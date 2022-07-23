Rough Ellipsoid Structure Tools (REST)
===================================
.. image:: final1.jpg

**REST** is a Java GUI application package for generating realistic cosmic dust structures.
It uses the CALLTARGET function from DDSCAT to generate ELLIPSOIDS or SUPER-ELLIPSOIDS as base structure depending on the selected structure and shape parameters like the *radius*, *semi-axes* and *exponents*. The program asks the user to provide *seed* cells which are initial set of points randomly selected for the *material* and *space* from the base structure. Depending on the type and number of seeds generated, the code cuts the base structure into *STRONGLY DAMAGED SPHERE*, *ROUGH SURFACES*, *POKED STRUCTURES* and *ROUGH FRACTAL AGGREGATES* by measuring the distance of each point with respect to the *seed* points.

It uses the following algorithms :

        1. **Strongly Damaged Sphere (SDS)**
        2. **Rough Surface (RS)**
        3. **Poked Structure (PS)**
        4. **Rough Surface Super-ellipsoid (RS-SE)**
        5. **Poked Structure Super-ellipsoid (PS-SE)**
        6. **Rough Fractal Aggregates (RFA)**

It pulls data from the `Open Food Facts database <https://world.openfoodfacts.org/>`_
and offers a *simple* and *intuitive* API.

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   

Contents
--------

.. toctree::

   usage
   api
