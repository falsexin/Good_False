# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import csv

class JospiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('51job.csv', 'w', encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['name','gs_name','city','pub_date','salary'])

    def process_item(self, item, spider):

        print('JospiderPipeline', item)
        self.wr.writerow([item['name'],item['gs_name'],item['city'],item['pub_date'],item['salary']])
        return item

    def close_spider(self, spider):
        self.file.close()