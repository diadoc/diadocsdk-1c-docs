# -*- coding: utf-8 -*-


from sys import path as PATH_variable
from os import path
import pathlib as pl

html_static_path = ['../conf/_static']
html_style = 'css/diadoc 1C COM style.css'

PATH_variable.append(path.abspath('../conf/_extensions'))
extensions = [
    'sphinx_tabs.tabs',
    'custom_newsfeed',
    'CComDomain'
]
primary_domain = 'com-object'
source_suffix = '.rst'
exclude_patterns = []

master_doc = 'index'

project = u'1C Addin/COM Диадок API'
copyright = u'2022, Diadoc'
author = u'Diadoc'
version = '5'
release = '37'
language = 'ru'

htmlhelp_basename = '1CAddin, COM Диадок API'
todo_include_todos = False
html_show_sphinx = False
html_theme = 'sphinx_rtd_theme'
highlight_language = 'cpp'
pygments_style = 'vs'
html_search_language = 'en'