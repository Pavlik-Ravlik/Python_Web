import sys
import os
sys.path.append(os.path.abspath('..'))
project = 'Fast API'
copyright = '2023, Pavlik Ravlik'
author = 'Pavlik Ravlik'


extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'nature'
html_static_path = ['_static']
