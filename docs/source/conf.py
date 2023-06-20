# pylint: skip-file
# type: ignore

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
# Use this line if you chose to separate source and build directories
sys.path.insert(0, os.path.abspath('../..'))
# Use this line if you chose to NOT separate source and build directories
# sys.path.insert(0, os.path.abspath('..'))


project = 'Python Clean Architecture example'
copyright = '2023, Claudio Shigueo Watanabe'
author = 'Claudio Shigueo Watanabe'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
