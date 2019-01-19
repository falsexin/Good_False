# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibilispriderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    list_info_no = scrapy.Field()
    list_info_url = scrapy.Field()
    list_info_img_url = scrapy.Field()
    list_info_title = scrapy.Field()
    list_info_fenshu = scrapy.Field()
    list_info_cishu = scrapy.Field()
    list_info_pinglunshu = scrapy.Field()
    list_info_user = scrapy.Field()