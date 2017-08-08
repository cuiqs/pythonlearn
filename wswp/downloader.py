#!/usr/bin/python
# -*- coding:utf-8 -*-
from throttle import Throttle
import requests
import random


class Downloader:
	
	def __init__(self,delay=5,user_agent=None,num_retries=1,proxies=None,cache=None):
		self.throttle=Throttle(delay)
		self.user_agent=user_agent
		self.proxies=proxies
		self.num_retries=num_retries
		self.cache=cache
	
	def __call__(self,url):
		result=None
		if self.cache:
			try:
				result=self.cache[url]
			except KeyError:
				pass
			else:
				if self.num_retries>0 and 500<reuslt['code']<600:
					#server error so ignore result from cache
					#and re-download
					result=None
		
		if result is None:
			#result is not get from cache
			self.throttle.wait(url)
			proxy=random.choice(self.proxies) if self.proxies else None
			headers={'User-agent':self.user_agent}
			result=self.download(url,headers,proxy,self.num_retries)
			
			if self.cache:
				#save result to cache
				self.cache[url]=result

		return result['html']
	
	def download(self,url,headers,proxy,num_retries,data=None):
		
		while num_retries>0:
			try:
				r=requests.get(url,headers=headers,proxies=proxy)
				return {'html':r.text,'code':r.status_code}
			except requests.exceptions.RequestException:
				num_retries-=1



