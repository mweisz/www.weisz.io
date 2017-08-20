#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michael Weisz'
SITENAME = "Michael's Blog"
SITEURL = ''
SITETITLE = 'Michael\'s Blog'
SITESUBTITLE = 'Computer Science Student at Oxford'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Blog Home', '#'),
#          )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Use my theme
THEME = 'themes/my-flex'
CUSTOM_CSS = 'theme/stylesheet/my_styles.css'

# Flex Theme Settings
SHOW_TAG_CLOUD = True
SHOW_RECENT_ARTICLES_IN_SIDEBAR = True

