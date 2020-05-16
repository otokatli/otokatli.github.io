#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ozan Tokatli'
SITENAME = u'Notes from the Underground'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/otokatli'),
          ('Github', 'https://github.com/otokatli'),
          ('LinkedIn', 'https://www.linkedin.com/in/ozan-tokatli'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
PATH = 'content'
ARTICLE_PATHS = ['articles',]
PAGE_PATHS = ['pages',]
MENUITEMS = (
    ('Home', '/index.html'),
    ('Publications', '/pages/publications.html'),
)
PLUGINS = ['pelican_bib',]
PUBLICATIONS_SRC = 'content/pubs.bib'
THEME_TEMPLATES_OVERRIDES = ['content/templates',]
