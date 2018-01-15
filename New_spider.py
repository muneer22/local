# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.selector import HtmlXPathSelector
# from scrapy.item import Item
# from scrapy.spiders import BaseSpider
# from scrapy import Request
# from scrapy.http import Request
# from scrapy.utils.httpobj import urlparse


# class MySpider(CrawlSpider):
# 	name = "New"
# 	allowed_domains = ['quotes.toscrape.com']

# 	start_urls = [
# 		'http://quotes.toscrape.com/page/1/',
# 	]

#	rules = (

		#Rule(SgmlLinkExtractor(allow=('category\.php'),restrict_css=('a.button.next')),callback="parse_items",follow=True),
		#Extract links matching 'Newy.php' (but not matching 'subsection.php')
		# & follow links from them(since no calback means follow = True by default).
#		Rule(LinkExtractor(allow=('container\.php',), deny=('div\.php',)), ),

		#Extract link matching  & parse them with the spider's method parse_item
#		Rule(LinkExtractor(), callback = 'parse_item',),
#		)

#	def parse_item(self, response):
#		for quote in response.css('div.quote'):
#			yield {
#				'text':quote.css('span.text::text').extract_first(),
#				'author':quote.css('small.author::text').extract_first(),
#				'tags':quote.css('row.tags a.tag::text').extract(),
#			}	

#			if not(all(quote.value())):
#				raise DropItem()
			#else:
				#return item
			
		
#from scrapy.exceptions import DropItem

#class DropIfEmptyFieldPipeline(object):

	
#	def process_item(self, item, spider):
		
#		if not(all(item.values())):
#			raise DropItem()
#		else:
#			return item
	
		#next_page = response.css('li.next a::attr(href)').extract_first()
		#if next_page is not None:
		#	next_page = response.urljoin(next_page)
		#yield scrapy.Request(next_page, callback=self.parse)
	#	return item 

#	def parse_item(self, response):
#		self.logger.info('Hi, this is an item page! %s', css.url)
#		for quote in response.css('div.quote'):
			
			#item = scrapy.Item()
#			item['text'] = quote.css('span.text::text').extract_first(),
#			return item





       # def __init__(self, url=None, *args, **kwargs):
        #    super(MySpider, self).__init__(*args, **kwargs)
         #   self.allowed_domains = [url]
          #  self.start_urls = ["http://" + url]

#        rules = [
#        Rule(SgmlLinkExtractor(allow=()), callback='parse_item')
#        ]

#        def parse_item(self, response):
 #           x = HtmlXPathSelector(response)
 
  #          filename = "output.txt"
  #          open(filename, 'ab').write(response.url + "\n")
#  			for quote in response.css('div.quote'):
#  				yield {
# 					'text':quote.css('span.text::text').extract(),
# 					'author':quote.css('small.author::text').extract_first(),
# 					'tags':quote.css('div.tags a.tag::text').extract(),
# 				}	
# #
# 			next_page = response.css('li.next a::attr(href)').extract_first()
# 			if next_page is not None:
# 				yield response.follow(next_page, callback=self.parse)


# print ("Crawling site...")
# print ("See output.txt for links")