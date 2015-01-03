#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Basic
AUTHOR = u'cosmoslx'
AUTHOR_EMAIL = 'cosmoslx@gmail.com'
#SITENAME = u'Cosmos of Cosmoslx'
SITENAME = u'A Ordinary Boy, A Marvelous Toy'
SITESUBTITLE = u'Story about a ordinary boy who want to build a marvelous toy'
SITESUBTITLES = ('A ordinary boy', 'build a marvelous toy')
SITEURL = 'http://blog.cosmoslx.me'
RELATIVE_URLS = False

TIMEZONE = 'Asia/Chongqing'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = u'zh'

DELETE_OUTPUT_DIRECTORY = True

SUMMARY_MAX_LENGTH = 20

# Category
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'General'

# Feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Theme
#THEME = 'franticworld'
THEME = 'bold'
TYPOGRIFY = True
#CSS_FILE = "wide.css"

# PATH
PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Plugin
PLUGIN_PATHS = ["/home/cosmoslx/github/pelican-plugins"]
PLUGINS = ["cjk-auto-spacing", "gravatar", "summary",]
SUMMARY_END_MARKER = "<!-- more -->" # keep compatible with octopress

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (('about me', 'http://about.me/cosmoslx'),
          ('github', 'http://github.com/cosmoslx'),
          )

# Following items are often useful when publishing

DISQUS_SITENAME = "cosmoslx-blog"
GOOGLE_ANALYTICS = "UA-58180786-1"
