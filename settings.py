# -*- coding: utf-8 -*-
#: settings for liquidluck

#: posts lay here
source = 'content'

#: generate html to ouput
output = '_site'
static_output = '_site/static'
# static_prefix = '/static/'

#: theme, load theme from _themes
theme = 'moment'
permalink = '{{category}}/{{filename}}/'
timezone = '+08:00'


#: site information
site = {
    'name': 'Just lepture',
    'url': 'http://lepture.com',
    'feed': 'http://feeds.lepture.com/lepture',
    'showtag': True,
}
author = 'lepture'
authors = {
    'lepture': {
        'name': 'Hsiaoming Yang',
        'website': 'http://lepture.com',
        'email': 'lepture@me.com',
    }
}

#: active readers
# readers = {}

#: active writers
writers = {
    'tag': None,
    'tagcloud': 'liquidluck.writers.core.TagCloudWriter'
}

writers_variables = {
    'archive_output': 'archive.html',
}

#: template variables for rewrite themes variables
template_variables = {
}

#: template filters
template_filters = {
}

#: theme variables
theme_variables = {
    'disqus': 'lepture',
    'analytics': 'UA-21475122-1',

    'allow_comment_on_secret_post': True,

    'navigation': [
        ('Blog', '/archive/'),
        ('Life', '/life/'),
        ('Work', '/work/'),
        (u'Résumé', '/resume/'),
    ],
    'elsewhere': [
        ('GitHub', 'https://github.com/lepture'),
        ('Twitter', 'https://twitter.com/lepture'),
    ],

    'descriptions': {
        'life': u'生命是一襲華美的袍，爬滿了虱子 －－ 張愛玲',
        'work': 'works in python, javascript, vim, and everything else'
    },
}
