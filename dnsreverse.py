#!/usr/bin/env python
# Performs a reverse lookup on the IP address given on the command line

import sys,socket

def getipaddrs(hostname)
	"""Get a list of IP address from a given hostname. this is a standard\	
	(forward) lookup"""
	result=socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)
	return [x[4][0] for x in result]

