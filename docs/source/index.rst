Rough Ellipsoid Structure Tools (REST)
===================================

**REST** is a Java GUI application package for generating realistic cosmic dust structures.
It generates the following structures
It pulls data from the `Open Food Facts database <https://world.openfoodfacts.org/>`_
and offers a *simple* and *intuitive* API.

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   The overall understanding of cosmic dust particles is mainly inferred from the different Earth-based measurements of interplanetary dust partilces (IDPs) and space missions such as Gitto, Stardust and Rosetta. The results from these measurements indicate presence of a wide variety of morphologically significant dust particles. To interpret the light scattering and thermal emission observations arising due to dust in different regions of space, it is necessary to generate computer modelled realistic dust structures of various shape, size, porosity, bulk density, aspect ratio and compositional inhomogenity. The present work introduces a java package called Rough Ellipsoid Structure Tool (REST), which is a collection of multiple algorithms, that aims to craft realistic rough surface cosmic dust particles from spheres, super-ellipsoids and fractal aggregates depending on the measured bulk-density and porosity. Initially, spheres having $N_d$ dipoles or lattice points are crafted by selecting random material and space seed cells to generate strongly damaged structure (SDS), rough surface (RS) and poked structure (PS). Similarly, REST generates rough surface super ellipsoids (RS-SE) and poked structure super-ellipsoids (PS-SE) from initial super-ellipsoid structures. REST also generates rough fractal aggregates (RFA) which are fractal aggregates having rough surface irregular grains/monomers from fractal aggregates of spheres (FA). Finally, REST has been used to create agglomerated debris (AD), agglomerated debris super-ellipsoids (AD-SE) and mixed morphology (RFA-AD) and the light scattering properties of the respective structures are studied to ensure their applicability. REST is a highly flexible structure tool, with the help of which users can generate various type dust structures that can be applied to study the physical properties of dust in different regions of space.

Contents
--------

.. toctree::

   usage
   api
