#!/usr/bin/env python

import os

print "Content-Type: text/html"
print

print "<pre>"
for key, value in os.environ.items():
	print key
	print "\t", value

