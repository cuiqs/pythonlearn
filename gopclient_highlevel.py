#!/usr/bin/env python
# High-Level Gopher Client -Chapter 1 -gopherlibclient.py

import urllib,sys
host=sys.argv[1]
file=sys.argv[2]

f=urllib.urlopen('gopher://%s%s' %(host,file))
for line in f.readlines():
	sys.stdout.write(line)

