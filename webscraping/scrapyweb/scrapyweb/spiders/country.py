#-*-coding:utf-8 -*-

import scrapy
from scrapyweb.items import ScrapywebItem

class country(scrapy.Spider):
	name='countryspider'
	allowed_domains=["example.webscraping.com"]

	start_urls=["http://example.webscraping.com/places/default/index/"+str(x) for x in range(1,26)]

	def parse(self,response):
		for td in response.xpath('//td'):
			url="http://example.webscraping.com"+td.xpath('./div/a/@href').extract_first()
			yield scrapy.Request(url,callback=self.parse_country)


	def parse_country(self,response):
		item=ScrapywebItem()
		table=response.xpath('//table')
		area=table.xpath('./tr[@id="places_area__row"]/td[2]/text()').extract()
		if area:
			item['area']=area
		
		population=table.xpath('./tr[@id="places_population__row"]/td[2]/text()').extract()
		if population:
			item['population']=population
		iso=table.xpath('./tr[@id="places_iso__row"]/td[2]/text()').extract()
		if iso:
			item['iso']=iso

		country=table.xpath('./tr[@id="places_country__row"]/td[2]/text()').extract()
		if country:
			item['country']=country

		capital=table.xpath('./tr[@id="places_capital__row"]/td[2]/text()').extract()
		if capital:
			item['capital']=capital

		currency=table.xpath('./tr[@id="places_currency_name__row"]/td[2]/text()').extract()
		if currency:
			item['currency']=currency

		phone=table.xpath('./tr[@id="places_area__row"]/td[2]/text()').extract()
		if phone:
			item['phone']=phone

		yield(item)
