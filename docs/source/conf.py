# Configuration file for the Sphinx documentation builder.

# -- Project information
import datetime
import locale
import os
import sys

project = 'REST'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration
html_static_path = ['_static'] 

def setup(app):
    app.add_css_file('style1.css')
    
# Otherwise VTK reader issues on some systems, causing sphinx to crash. See also #226.
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

if sys.version_info >= (3, 0):
    import faulthandler

    faulthandler.enable()

sys.path.insert(0, os.path.abspath("."))
import make_external_gallery
import make_tables

make_external_gallery.make_example_gallery()
make_tables.make_all_tables()

# -- pyvista configuration ---------------------------------------------------
import pyvista

# Manage errors
pyvista.set_error_output_file("errors.txt")
# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True  # Not necessary - simply an insurance policy
# Preferred plotting style for documentation
pyvista.set_plot_theme("document")
pyvista.global_theme.window_size = [1024, 768]
pyvista.global_theme.font.size = 22
pyvista.global_theme.font.label_size = 22
pyvista.global_theme.font.title_size = 22
pyvista.global_theme.return_cpos = False
pyvista.set_jupyter_backend(None)
# Save figures in specified directory
pyvista.FIGURE_PATH = os.path.join(os.path.abspath("./images/"), "auto-generated/")
if not os.path.exists(pyvista.FIGURE_PATH):
    os.makedirs(pyvista.FIGURE_PATH)

# necessary when building the sphinx gallery
pyvista.BUILDING_GALLERY = True
os.environ['PYVISTA_BUILDING_GALLERY'] = 'true'

# SG warnings
import warnings

warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message="Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.",
)


# -- General configuration ------------------------------------------------
numfig = False
html_logo = "./_static/pyvista_logo_sm.png"

sys.path.append(os.path.abspath("./_ext"))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "jupyter_sphinx",
    "sphinx_panels",
    "pyvista.ext.plot_directive",
    "pyvista.ext.coverage",
    "numpydoc",
    "sphinx.ext.viewcode",
    "myst_nb"
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}

jupyter_execute_notebooks = "auto"

latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
