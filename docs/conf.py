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
                       'highcharts_core',
                       '__version__.py')) as version_file:
    exec(version_file.read(), version_dict)                   # pylint: disable=W0122

__version__ = version_dict.get('__version__')


project = 'Highcharts Core for Python'
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
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_tabs.tabs',
    'sphinx_toolbox.shields',
    'sphinx_toolbox.decorators',
    'sphinx_toolbox.issues',
    'sphinx_toolbox.formatting',
    'sphinx_toolbox.collapse',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Autodoc configuration settings.
autoclass_content = 'class'
autodoc_member_order = 'groupwise'
add_module_names = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 3,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    'style_nav_header_background': 'rgb(70, 70, 92)'
}

html_css_files = [
    'sphinx_rtd_theme_ext_color_contrast.css'
]

html_js_files = [
    'https://code.jquery.com/jquery-3.6.4.min.js'
]

html_logo = '_static/highcharts-for-python-light-150x149.png'
html_favicon = '_static/highcharts-for-python-dark-32x32.png'

html_context = {
    "display_github": True,                 # Integrate GitHub
    "github_user": "highcharts-for-python",       # Username
    "github_repo": "highcharts-core",     # Repo name
    "github_version": "master",             # Version
    "conf_py_path": "/docs/",               # Path in the checkout to the docs root
}

github_username = 'highcharts-for-python'
github_repository = 'highcharts-core'

sphinx_tabs_disable_tab_closing = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.10', None),
    'validator-collection': ('http://validator-collection.readthedocs.io/en/latest/', None),
    'ipython': ('https://ipython.readthedocs.io/en/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'pyspark': ('https://spark.apache.org/docs/latest/api/python/', None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Inheritance Diagram configuration
inheritance_graph_attrs = {
    'rankdir': 'TB'
}

suppress_warnings = [
    # 'ref.term',
    'ref.ref',
    'toc.not_readable'
]
