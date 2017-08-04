# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapywebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	area=scrapy.Field()
	population=scrapy.Field()
	iso=scrapy.Field()
	capital=scrapy.Field()
	country=scrapy.Field()
	currency=scrapy.Field()
	phone=scrapy.Field()
