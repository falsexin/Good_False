# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 岗位
    name = scrapy.Field()
    # 公司名
    gs_name = scrapy.Field()
    # 城市
    city = scrapy.Field()
    #日期
    pub_date = scrapy.Field()
    # 薪资
    salary = scrapy.Field()




