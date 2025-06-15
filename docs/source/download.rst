Download
========

This page provides instructions for downloading and installing the Windows version of the **REST** (Rough Ellipsoid Structure Tools) package, along with its system requirements and citation information.

.. contents::
   :local:
   :depth: 2

----

📥 Download REST for Windows
----------------------------

You can download the latest Windows release from the GitHub Releases page:

🔗 **Download**:  
`REST-Windows.zip <https://github.com/prithishh3/REST/releases/latest>`_

1. Click the link above to download the archive.
2. Extract the contents to a convenient folder.
3. Double-click `REST.bat` inside the `REST-Windows` directory to launch the GUI.

.. note::
   Make sure Java 11 or later is installed on your system.

----

💻 Platform Support
-------------------

REST is designed to be cross-platform:

+-----------+-----------+------------------------------+
| Platform  | Supported | Notes                        |
+===========+===========+==============================+
| Windows   | ✅        | `.bat` launcher included     |
+-----------+-----------+------------------------------+
| Linux     | ✅        | Release coming soon          |
+-----------+-----------+------------------------------+
| macOS     | ✅        | Release coming soon          |
+-----------+-----------+------------------------------+

----

⚙️ Requirements (Windows)
--------------------------

To run REST and its plotting features:

- Java 11 or newer
- Python 3.x
- PyVista (install via `pip install pyvista`)
- VTK (install via `pip install vtk`)
- `gfortran` (required to run `calltarget` and generate composite structures)

.. important::
   For `.sh` scripts and DDSCAT integration (optional), install **Windows Subsystem for Linux (WSL)**:  
   https://learn.microsoft.com/en-us/windows/wsl/install

----

🚀 Usage
--------

To get started after downloading and extracting:

1. Ensure all dependencies are installed.
2. Run `REST.bat` (for Windows) to launch the GUI.
3. Use the GUI to generate structures, save `.target` files, and visualize results.

For structure-specific scripts and command-line use, see the *Usage* section in the documentation.

----

📚 Citation
-----------

If you use REST in your research, please cite the following publication:

**Halder, P. (2022)**  
*REST: A Java Package for Crafting Realistic Cosmic Dust Particles*.  
*The Astrophysical Journal Supplement Series*, **263**(1), 3.  
DOI: https://doi.org/10.3847/1538-4365/ac9183

**BibTeX:**

.. code-block:: bibtex

   @article{Halder_2022,
     doi = {10.3847/1538-4365/ac9183},
     url = {https://dx.doi.org/10.3847/1538-4365/ac9183},
     year = {2022},
     month = {oct},
     publisher = {The American Astronomical Society},
     volume = {263},
     number = {1},
     pages = {3},
     author = {Halder, Prithish},
     title = {REST: A Java Package for Crafting Realistic Cosmic Dust Particles},
     journal = {The Astrophysical Journal Supplement Series}
   }

----

📖 Full Documentation
----------------------

For detailed usage instructions, structure generation workflows, and troubleshooting:

🔗 https://rest-package.readthedocs.io/en/latest/
