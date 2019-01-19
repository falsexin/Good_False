# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import csv

class BilibilispriderPipeline(object):
    def __init__(self):
        self.file = codecs.open('bilibili.csv', 'w', encoding='utf-8')
        self.wr = csv.writer(self.file)

        self.wr.writerow(['list_info_no','list_info_url','list_info_img_url','list_info_title','list_info_fenshu','list_info_cishu','list_info_pinglunshu',['list_info_user']])

    def process_item(self, item, spider):

        # print('JospiderPipeline', item)
        self.wr.writerow([item['list_info_no'],item['list_info_url'],item['list_info_img_url'],item['list_info_title'],item['list_info_fenshu'],item['list_info_cishu'],item['list_info_pinglunshu'],item['list_info_user']])
        return item

    def close_spider(self, spider):
        self.file.close()
