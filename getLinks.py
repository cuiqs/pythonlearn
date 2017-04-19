#!/usr/bin/env python
# Get all of links in the webpage

import sys,urllib2,re
from HTMLParser import HTMLParser

class getLinker(HTMLParser):
	def __init__(self):
		self.links=[]
		HTMLParser.__init__(self)
	
	def handle_starttag(self,tag,attrs):
		if tag=='link'or tag=='a':
			if len(attrs)==0:
				pass
			else:
				for(variable,value) in attrs:
					if variable=='href':
						self.links.append(value)
						print value


url=sys.argv[1]
req=urllib2.Request(url)
fd=urllib2.urlopen(req)

data=fd.read()
#print data
parser=getLinker()
parser.feed(data)
#print parser.links

