from scrapy.spiders import Spider
from scrapy.selector import Selector
from craiglist_sample.items import CraiglistSampleItem
from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class MySpider(CrawlSpider):
	name = "test"
	allowed_domains=["craigslist.org"]
	start_urls = ["http://sfbay.craigslist.org/search/npo"]

	rules = (
		Rule(SgmlLinkExtractor(allow=(),restrict_css=('a.button.next')),callback="parse_items",follow=True),
		)


	def parse_items(self,response):
		# hxs = Selector(response)
		# titles = hxs.xpath("//span[@class='p1']")
		# items =[]
		# for titles in titles:
		# 	item = CraiglistSampleItem()
		# 	item["title"] = titles.xpath("a/text()").extract()
		# 	item["link"] = titles.xpath("a/@href").extract()
		# 	items.append(item)
		# return items

		#titles = response.css("p.result-info").extract()
		
		
		
		titles = response.css("li.result-row p.result-info a::text").extract()
		links = response.css("li.result-row p.result-info a::attr('href')").extract()
			
		info = zip(titles,links)
		items =[]
		for group in info:

			if group[1] != "#" and "\n" not in group[0]: 
				 item = CraiglistSampleItem()
				 item["title"] = group[0]
				 item["link"] = group[1]
				 items.append(item)

		print items


		return items