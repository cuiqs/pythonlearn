# !/usr/bin/python
# -*- coding:utf-8 -*-
import datetime
import requests
class Throttle:
	"Add a delay between downloads to the same domain"""
	
	def __init__(self,delay):
		#amount of delay between download for each domain
		self.delay=delay
		self.domains={}
	
	def wait(self,url):

		last_accessed=self.domains.get(url)
		
		if self.delay>0 and last_accessed is not None:
			sleep_secs=self.delay-(datetime.datetime.now()-last_accessed).seconds
			if sleep_secs>0:
				#The url has been accessed recently,need to wait 
				time.sleep(sleep_secs)
		
		self.domains[url]=datetime.datetime.now()

