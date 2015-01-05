#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False

AUTHOR = u'cosmoslx'
AUTHOR_EMAIL = 'cosmoslx@gmail.com'
#SITENAME = u'Cosmos of Cosmoslx'
SITENAME = u'A Ordinary Boy, A Marvelous Toy'
SITESUBTITLE = u'Story about a ordinary boy who want to build a marvelous toy'
SITESUBTITLES = ('A Ordinary Boy', 'A Marvelous Toy')
SITEURL = 'http://blog.cosmoslx.me'
TOYURL = 'http://github.com/cosmoslx/blog'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'General'

TIMEZONE = 'Asia/Chongqing'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = u'zh'

SUMMARY_MAX_LENGTH = 20

# Theme
#THEME = 'SoMA2'
#THEME = 'Responsive-Pelican'
THEME = 'bold'
#THEME = 'franticworld'
#THEME = 'fresh'
TYPOGRIFY = True
#CSS_FILE = "wide.css"

# PATH
PATH = 'content'
STATIC_PATHS = ['images', 'extra',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/baidu_verify_an3X8DDsE3': {'path': 'baidu_verify_an3X8DDsE3.html'},
                       }

# Plugin
PLUGIN_PATHS = ["/home/cosmoslx/github/pelican-plugins"]
PLUGINS = ["cjk-auto-spacing", "gravatar", "summary","sitemap",]
SUMMARY_END_MARKER = "<!-- more -->" # keep compatible with octopress
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    },
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (('about me', 'http://about.me/cosmoslx'),
          ('github', 'http://github.com/cosmoslx'),
          )

DEFAULT_PAGINATION = 10
