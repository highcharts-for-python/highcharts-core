# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__name__), '..'))


version_dict = {}
with open(os.path.join(os.path.dirname(__file__),
                       '../',
                       'highcharts',
                       '__version__.py')) as version_file:
    exec(version_file.read(), version_dict)                   # pylint: disable=W0122

__version__ = version_dict.get('__version__')


project = 'Highcharts for Python'
copyright = '2022, HCP LLC'
author = 'Chris Modzelewski'

# The short X.Y version
version = __version__[:3]
# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_tabs.tabs'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 3,
    'display_version': True,
    'prev_next_buttons_location': 'both'
}

html_logo = '_static/highcharts-python-logo-100x50.png'
html_favicon = '_static/highcharts-python-logo-32x32.png'


html_context = {
    "display_github": True,                 # Integrate GitHub
    "github_user": "insightindustry",       # Username
    "github_repo": "highcharts-python",     # Repo name
    "github_version": "master",             # Version
    "conf_py_path": "/docs/",               # Path in the checkout to the docs root
}
