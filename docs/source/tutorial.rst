Tutorial
========

.. _installing_dependencies:

Installing Dependencies
-----------------------
1. **Installing Java 11**
   The different ways to install **Java 11** on different distros are shown below:
   
   **Ubuntu**

   .. code-block:: console

      $ sudo apt-get install openjdk-11-jdk

   **Fedora**
   
   .. code-block:: console
   
      $ sudo dnf install java-11-openjdk -y
      
   **Mac** 
      
   .. code-block:: console
   
      $ sudo port install openjdk11
      
2. **Installing PyVista** (version - 0.29.0)

   PyVista can be installed from `PyPI <https://pypi.org/project/pyvista/>`_
   using ``pip`` on Python >= 3.7::

      pip install pyvista==0.29.0

   You can also visit `PyPI <https://pypi.org/project/pyvista/>`_,
   `Anaconda <https://anaconda.org/conda-forge/pyvista>`_, or
   `GitHub <https://github.com/pyvista/pyvista>`_ to download the source.

   See the `Installation <http://docs.pyvista.org/getting-started/installation.html#install-ref.>`_
   for more details regarding optional dependencies or if the installation through pip doesn't work out.
   
   
.. _input_parameters:

Input Parameters
----------------

The basic input parameters for **REST** are listed below:

   1. Type of structure
      
      * Strongly Damaged Sphere (SDS)
      * Rough Surface (RS)
      * Poked Structure (PS)
      * Rough Surface Super-ellipsoids (RS-SE)
      * Poked Structure Super-ellipsoids (PS-SE)
      * Rough Fractal Aggregates (RFA)
      
   2. Radius of initial spherical structure $R_d$     
      

     

