# -*- coding: utf-8 -*-


import sys
import os

sys.path.append(os.path.abspath('source/_extensions'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'custom_newsfeed',
    'CComDomain'
]


source_suffix = '.rst'
master_doc = 'source/index'
project = u'1C Addin/COM Диадок API'
copyright = u'2022, Diadoc'
author = u'Diadoc'
version = '5'
release = '37'
language = 'ru'
exclude_patterns = []
highlight_language = 'cpp'
pygments_style = 'vs'
todo_include_todos = False
html_theme_path = ['_themes']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_show_sphinx = False
html_search_language = 'en'
htmlhelp_basename = '1CAddin, COM Диадок API'
primary_domain = 'com-object'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}
latex_documents = [
  (master_doc, '{}.tex'.format(htmlhelp_basename), project, author, 'manual'),
]

man_pages = [
    (master_doc, htmlhelp_basename, project, [author], 1)
]

texinfo_documents = [
  (master_doc, htmlhelp_basename, project, author, htmlhelp_basename, 'Документация {}'.format(project), 'Miscellaneous'),
]

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']

intersphinx_mapping = {'https://docs.python.org/': None}
