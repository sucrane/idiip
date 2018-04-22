#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

OUTPUT_PATH = 'docs/'
SITEURL = 'http://www.jiinii.com/idiip'

GOOGLE_ANALYTICS = "UA-117999375-1"

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-8599880473432439',     # Your AdSense ID
    'page_level_ads': True,                 # Allow Page Level Ads (mobile)
    'ads': {
    #     'aside': '1234561',               # Side bar banner (all pages)
    #     'main_menu': '1234562',           # Banner before main menu (all pages)
    #     'index_top': '1234563',           # Banner after main menu (index only)
    #     'index_bottom': '1234564',        # Banner before footer (index only)
    #     'article_top': '1234565',         # Banner after article title (article only)
    #     'article_bottom': '1234566',      # Banner after article content (article only)
    }
}