#!/usr/bin/env python
# Obtain web page --dump_page.py

import sys,urllib2,os

#print os.environ['http_proxy']

req=urllib2.Request(sys.argv[1])
try:
	fd=urllib2.urlopen(req)
	while 1:
		data=fd.read(1024)
		if not len(data):
			break
		sys.stdout.write(data)	
except urllib2.HTTPError,e:
	print e.code
	print e.reason
	print e.geturl()
	print e.read()
except urllib2.URLError,e:
	print e.reason


