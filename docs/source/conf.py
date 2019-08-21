# -*- coding: utf-8 -*-


import sys
import os

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'custom_newsfeed',
    'CComDomain'
]

sys.path.append(os.path.abspath('_extensions'))

source_suffix = '.rst'
master_doc = 'index'
project = u'AddIn Diadoc API'
copyright = u'2015, Diadoc'
author = u'Diadoc'
version = '1'
release = '1'
language = 'ru'
exclude_patterns = []
highlight_language = 'c#'
pygments_style = 'vs'
todo_include_todos = False
html_theme_path = ['_themes']
html_theme = 'custom_sphinx_rtd_theme'
html_static_path = ['_static']
html_show_sphinx = False
html_search_language = 'en'
htmlhelp_basename = '1CDiadocdoc'
primary_domain = 'comobject'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}
latex_documents = [
  (master_doc, '1CDiadoc.tex', u'1C Diadoc Documentation', author, 'manual'),
]

man_pages = [
    (master_doc, '1cdiadoc', u'1C Diadoc Documentation', [author], 1)
]

texinfo_documents = [
  (master_doc, '1CDiadoc', u'1C Diadoc Documentation', author, '1CDiadoc', 'One line description of project.', 'Miscellaneous'),
]

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']

intersphinx_mapping = {'https://docs.python.org/': None}
