import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import time
from selenium import webdriver
from scrapy.http import HtmlResponse
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.http import TextResponse


class MySpider(scrapy.Spider):
	name = "xsele"
	start_urls = [
		'https://www.apartmentguide.com/apartments/Maryland/Laurel/Briarwood-Place-Apartment-Homes/48001/'
	]

	def __init__(self):
		self.driver = webdriver.Chrome()
		

	def parse(self, response):
		self.driver.get(response.url)

# Code for contineously clicking Load more.
		try:
			while self.driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_1i1ia", " " ))]') is not None:
				button =  self.driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_1i1ia", " " ))]')
				button.click()
#				time.sleep(5)
		except Exception:
			pass

# Different types of retreving current page_source.

#		new = HtmlResponse(self.driver.current_url,body=self.driver.page_source,encoding='utf-8')
		#response = TextResponse(url= 'https://www.apartmentguide.com/apartments/Maryland/Laurel/Briarwood-Place-Apartment-Homes/48001/',body = self.driver.page_source,encoding='utf-8')
#		response = TextResponse(url= response.url, body = self.driver.page_source,encoding='utf-8')
#		new = HtmlXPathSelector(response.url, body = self.driver.page_source,encoding='utf-8')
#		new = HtmlXPathSelector(response)
		new = Selector(text=self.driver.page_source)
#		response = HtmlResponse(url='https://www.apartmentguide.com/apartments/Maryland/Laurel/Briarwood-Place-Apartment-Homes/48001/', )
#		Selector(response=response).xpath('p //*[contains(concat( " ", @class, " " ), concat( " ", "_140NQ", " " ))]').extract_first()
#		Selector(response = response)

# Retreving data through XPath.

#		for _140NQ in response.css("div._140NQ"):
		for _140NQ in new.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_140NQ", " " ))]'):
			item = scrapy.Field()
			item['Review'] =_140NQ.xpath('p //span//text()').extract_first(),
			item['Date'] = _140NQ.xpath('div //*[contains(concat( " ", @class, " " ), concat( " ", "_1GQMQ", " " ))]//text()').extract_first(),
			item['Author'] = _140NQ.xpath('div //*[contains(concat( " ", @class, " " ), concat( " ", "_3GPmB", " " ))]//text()').extract_first(),
# Retreiving data through css Selector.

			# item['Review'] =_140NQ.css("p span::text").extract_first(),
			# item['Date'] = _140NQ.css("div ._1GQMQ::text").extract_first(),
			# item['Author'] = _140NQ.css("div ._3GPmB::text").extract(),

#			print(item)
			yield item

