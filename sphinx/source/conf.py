# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import tomllib
from datetime import datetime
from pathlib import Path

# docs are in: transix/sphinx/
# package is in: transix/transix/
sys.path.insert(0, os.path.abspath("../.."))

pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"

with open(pyproject_path, "rb") as f:
    data = tomllib.load(f)

project = 'transix'
copyright = str(datetime.now().year)
author = 'Gowtham Mahendran'
release = data["project"]["version"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "numpydoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    ]
source_suffix = {
    ".rst": "restructuredtext",
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']
html_title = "transix"
# html_favicon = "_static/logo-square.svg"
html_last_updated_fmt = ""

html_theme_options = {
    "repository_url": "https://github.com/Gowtham-Mahendran/transix",
    "use_repository_button": True,
    "use_issues_button": True,
    # "logo": {
    #     "image_light": "_static/logo-light.png",
    #     "image_dark": "_static/logo-dark.png",
    #     "link": "some/other-page",
    # }
}