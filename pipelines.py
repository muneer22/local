# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#
#class TutorialPipeline(object):
 #   def process_item(self, item, spider):
  #      return item
#Setting pipeline to remove unicode characters & opening file with same name as that of spider
#from scrapy.exporters import JsonItemExporter
#from spiders.quotes2_spider import Quotes2Spider as spider

#class JsonWithEncodingPipeline(object):

#	def __init__(self):
#		self.file = open( spider.name + '.jl', 'wb')
#		self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False,)
#		self.exporter.start_exporting()

#	def spider_closed(self, spider):
#		self.exporter.finish_exporting()
#		self.file.close()

#	def process_item(self, item, spider):
#		self.exporter.export_item(item)
#		return item

# setting pipeline to remove unicode characters with codecs & opening & writing to a file automatically 
#import json
#import codecs
#from spiders.quotes2_spider import Quotes2Spider as spider


#class JsonWithEncodingPipeline(object):

#    def __init__(self):
#        self.file = codecs.open('quotes2.json', 'w', encoding='utf-8')

#    def process_item(self, item, spider):
#        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#        self.file.write(line)
#        return item

#    def spider_closed(self, spider):
#        self.file.close()


#from __future__ import unicode_literals
#import json 
#import codecs
#from spiders.quotes2_spider import Quotes2Spider as spider
#from scrapy.contrib.loader.processor import MapCompose

#class JsonWithEncodingPipeline(object):

#	def __init__(self):
#		self.file = codecs.open( spider.name +'.json', 'w', encoding='utf-8')

#	def process_item(self, item, spider):

#		print(json.dumps((item['text']), ensure_ascii=False) + "\n")

#		print("*********{}****".format(json.dumps((item['text']), ensure_ascii = False )+ "\n"))	
#		print("@@@@@@@@@@@@{}@@@@@@@@@@".format(json.dumps((item['author']), ensure_ascii = False )+ "\n"))	
#		print("#############{}######".format(json.dumps((item['tag']), ensure_ascii = False )+ "\n"))
		
#		text1 = json.dumps((item['text']), ensure_ascii = False )
	
#		auth = json.dumps((item['author']) )
	
#		tag = json.dumps((item['tag']), ensure_ascii = False )+ "\n"

#		line= (text1 + auth + tag)
#		print(line)
		
#		self.file.write(line)
		#return item

#	def spider_closed(self, spider):
#		self.file.close()


#
#from __future__ import unicode_literals
#import json 
#from spiders.quotes2_spider import Quotes2Spider as spider
#from scrapy.exporters import JsonLinesItemExporter


#class MyJsonLinesItemExporter(JsonLinesItemExporter):

#class JsonWithEncodingPipeline(object):
#	def __init__(self):
#		self.file = (self).__init__(file)

#	def process_item(self, item, spider, **kwargs):
#		if item:

	
    	#return item
#		if item['text']:
#			text1 = json.dumps((item['text']), ensure_ascii = False )
#			print("&&&&&&&&&&{}&&&&&&&&&".format(text1))
#			line = text1

#		self.file.write(line)	
#		return item
#		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
			#print str(item['text'][0]).encode("utf-8")
#			item['text'] =  str(item['text'][0]).encode("utf-8")

#			item['author'] = str(item['author'][0]).encode("utf-8")

#			item['tag'] = str(item['tag']).encode("utf-8")
			
#			print (item['text'])
#			print (item['author'])
#			print (item['tag'])
			#return item
