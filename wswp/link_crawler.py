#-*- coding:utf-8 -*-

import time 
from datetime import time
import Queue
import lxml.html
import requests
import throttle
from downloader import Downloader
import csv
import re

contents=['area','population','iso','country','capital','continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours']

def link_crawler(seed_url,link_regex=None,delay=5,max_depth=-1,max_urls=-1,headers=None,user_agent=None,num_retries=1,scrape_callback=None):
    """Crawl from the given seed URL following links matched by link_regex
    """
    #the queue of URL's that need to be crawled
    crawl_queue=[seed_url]
    #the URL's that have been seen and at what depth
    seen={seed_url:0}
    #track how many URL's have been downloaded
    num_urls=0
    thrdelay=throttle.Throttle(delay)
    headers=headers or {}
    if user_agent:
        headers['User_agent']=user_agent
    
    download=Downloader()
    while crawl_queue:
        url=crawl_queue.pop()
        depth=seen[url]
        html=download(url)
        print url+'is scraping'
        links=[]
        if scrape_callback:
            links.extend(scrape_callback(url,html) or [])
        
        if depth !=max_depth:
            if link_regex:
                #filter for links matching our regular expression
                links.extend(link for link in get_links(html) if re.match(link_regex,link))
            else:
                links.extend(get_links(html))

            for link in links:
                link=normalize(seed_url,link)
                if link not in seen.keys():
                    seen[link]=depth+1
                    crawl_queue.append(link)
        
        num_urls+=1
        if num_urls==max_urls:
            break

def normalize(seed_url,link):
    return seed_url+link

        
def get_links(html):
    tree=lxml.html.fromstring(html)
    links=[]
    atag=tree.cssselect('div.span12 a')
    for a in atag:
        links.append(a.get('href'))

    return links

class ScrapeCallback:
    def __init__(self):
        global contents
        self.writer=csv.writer(open('countries.csv','w'))
        self.fields=tuple(contents)
        self.writer.writerow(self.fields)
        
    def __call__(self,url,html):
        if re.search('/view/',url):
            tree=lxml.html.fromstring(html)
            row=[]
            for field in self.fields:
                row.append(tree.cssselect('table>tr#places_{}__row>td.w2p_fw'.format(field))[0].text_content())
            self.writer.writerow(row)

        
link_crawler('http://example.webscraping.com',scrape_callback=ScrapeCallback())   
