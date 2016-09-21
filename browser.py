#!/usr/bin/env python

import os

user_agent = os.environ['HTTP_USER_AGENT']

print "Content-Type: text/html"
print

if 'Chrome' in user_agent:
	print "You're using chrome!"
elif 'Firefox' in user_agent:
	print "You're using firefox!"	
else:
	print "I don't know what you're using."
