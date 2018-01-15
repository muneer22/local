from __future__ import unicode_literals
import scrapy
#import os
#import string
import sys
reload(sys)
sys.setdefaultencoding('utf8')



class Quotes2Spider(scrapy.Spider):
	name = "quotes2"
	start_urls = [
		'http://quotes.toscrape.com/page/1/'
		]

	def parse(self, response):
		for quote in response.css('div.quote'):
#			yield{
			item = scrapy.Field()
			item['text'] = quote.css('span.text::text').extract_first(),
			item['author']= quote.css('small.author::text').extract_first(),
			item['tag'] = quote.css('div.tags a.tag::text').extract(),
#			}
# Removing unicode characters in spider itself by encoding to ascii.
#			item['text'] = quote.css('span.text::text').extract_first().encode('ascii', 'ignore'),
#			item['author']= quote.css('small.author::text').extract_first().encode('ascii', 'ignore'),
#			item['tag'] = quote.css('div.tags a.tag::text').extract().encode('ascii', 'ignore'),
			yield item
	
		next_page = response.css('li.next a::attr(href)').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)

				#yield item			







