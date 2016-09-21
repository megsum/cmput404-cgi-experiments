#!/usr/bin/env python

import os

user_agent = os.environ["HTTP_USER_AGENT"]

print "Content-Type: text/html"
print

if 'Chrome' in user_agent:
    print 'Chrome'
elif 'Firefox' in user_agent:
    print "Firefox"
else:
    print "????"
