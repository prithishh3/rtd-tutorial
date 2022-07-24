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
      
2. **Installing PyVista**

   PyVista can be installed from `PyPI <https://pypi.org/project/pyvista/>`_
   using ``pip`` on Python >= 3.7::

      pip install pyvista

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
      
   2. Radius of initial spherical structure R\ :sub:`d` (for the SDS, RS and PS structures)
   3. Semi-axes *a*, *b* and *c* (for RS-SE and PS-SE structures)
   4. East-west exponent *e* and north-south exponent *n* (for the RS-SE and PS-SE structures)
   5. Coordinates in the format *[r, X, Y, Z, material_tag]* where *r* is the radius of each grain of a fractal aggregate and *material_tag* is 1 for                         homogeneous material and 1 or 2 for inhomogeneous material (for RFA structures)
   6. Number of material seed cells *N*\ :sub:`m`
   7. Number of space seed cells *N*\ :sub:`s`
   8. Number of surface seed cells *N*\ :sub:`ss`
   9. Thickness of surface layer *t*
   10. Final structure file *name*
   

.. _strongly_damaged_sphere:

Strongly Damaged Sphere (SDS) [*Default Seeds*]
--------------------------------------------

   1. Select the option **Strongly Damaged Sphere**. Upon selecting an option the input panel appears as shown below.

   .. image:: er3.png

   2. Select the **Default Seeds** option from the input panel. Enter the *Radius* of initial structure in number of dipoles (e.g. R\ :sub:`d`\ = 32) and         enter a      filename for the final structre in the **File name** section of the input panel. Finally click the **Calculate** button to start the           calculation.        During calculation an **xterm** window will open and indicate the progress of calculation as shown below.

   .. image:: er4.png

   3. Upon completion of the calculation, the control box will appear below the input panel having *pink* border.

   .. image:: er5.png

   4. Click the **Final structure data** button to import the data calculated for generating the final **SDS** structure in the **Structure file** panel on       the right-hand side.

   .. image:: er7.png

   5. Finally, click the **3D Plot** button to convert all the structure data into *VTK* files and generate the 3D structures initial and final structure      along with the distribution of the different seed cells within the initial structure.

   .. image:: e8.png

   6. Save the structure data by clicking **Save data** button and save the 3D plot by clicking **Save plot** button. 
   7. Reset or clear the input and output entries by clicking **Clear & Reset** button.

.. _strongly_damaged_sphere_custom:

Strongly Damaged Sphere (SDS) [*Custom Seeds*]
----------------------------------------------
   1. In case of SDS (*Custom seed*) option select **Custom Seeds**.
   2. Enter the values for **Intitial radius of the sphere** (R\ :sub:`d`\), **No. of Material seed cells** (N\ :sub:`m`\) and **No. of Space seed              cells** (N\ :sub:`s`\).
   3. Enter the **File name** and hit **Calculate** button.


.. _rough_surface:

Rough Surface (RS)
------------------

.. _poked_structures:

Poked Structures (PS)
---------------------

.. _rough_surface_super-ellipsoids:

Rough Surface Super-ellipsoids (RS-SE)
--------------------------------------

.. _poked_structure_super-ellipsoids:

Poked Structure Super-ellipsoids (PS-SE)
----------------------------------------


     

