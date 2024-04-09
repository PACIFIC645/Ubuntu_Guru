import os
import sys
import django

sys.path.insert(0, os.path.abspath('..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

# Sphinx settings
project = 'Ubuntu_Guru'
copyright = '2024, Kgaogelo Lekganyane'
author = 'Kgaogelo Lekganyane'
release = 'April 2024'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # If you use Google or NumPy style docstrings
    'sphinx.ext.viewcode',  # Optionally add to include source code links
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']
