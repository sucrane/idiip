#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Su Henian'
SITENAME = 'idiip site'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Asia/Hong_Kong'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'articles'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGINS = ['neighbors']

THEME = 'Flex'
PYGMENTS_STYLE = 'solarized-dark'
SITETITLE = 'idiip'
SITESUBTITLE = 'I did it in Python.'
SITEDESCRIPTION = 'Python is an amazing language, so I put every stuff that can be done in Python to this site.'
SITELOGO = 'https://www.gravatar.com/avatar/8b7b3f139824eb533c0650e33d44067b?s=200'

MAIN_MENU = True
DISABLE_URL_HASH = True
COPYRIGHT_NAME = 'Jiinii.com'
COPYRIGHT_YEAR = 2018