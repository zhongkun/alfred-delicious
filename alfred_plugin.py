# -*- coding:utf-8 -*-

from feedback import Feedback
from deliciousapi import DeliciousAPI
import sys
import re
import urllib2
import urllib

query = '{query}'
d = DeliciousAPI()

user = d.get_user('kun77416', None, query)
fb = Feedback()

i = 0
try:
    for b in user.bookmarks:
        tags = tuple(b[1])
        fb.add_item(b[2],subtitle=str(tags), uid=i, arg=b[0])

except SyntaxError as e:
    if ('EOF', 'EOL' in e.msg):
        fb.add_item('...')
    else:
        fb.add_item('SyntaxError', e.msg)
except Exception as e:
        fb.add_item(e.__class__.__name__,
            subtitle=e.message) 

print fb

