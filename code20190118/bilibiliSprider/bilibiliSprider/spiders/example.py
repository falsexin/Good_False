# -*- coding: utf-8 -*-
import scrapy
import re
import json
from ..items import BilibilispriderItem

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/0/0/7/']

    def parse(self, response):
        # print(response.body)
        pic = response.selector.re('window.__INITIAL_STATE__=(.*);\(function')[0]
        # a = re.search('window.__INITIAL_STATE__.*?',response.body)
        pic = json.loads(pic)['rankList']
        # print(type(a), dir(a))
        info = response.xpath('//ul[@class="rank-list"]/li[@class="rank-item"]')
        # print(len(info))
        for list_info in info:
            list_info_no = list_info.xpath('./div[@class="num"]/text()').extract()[0]
            print('序号：', list_info_no)
            list_info_url = list_info.xpath('.//div[@class="img"]//a/@href').extract()[0]
            print('序号链接：', list_info_url)
            a = re.findall('\d+', list_info_url)[0]
            list_info_img_url = '无'
            list_info_user = '无'
            for i in pic:
                # print(i['aid'])
                if a == i['aid']:
                    list_info_user = i['author']
                    list_info_img_url = i['pic']
                    print('图片链接：', list_info_img_url)
            # list_info_img_url = list_info.xpath('.//div[contains(@class, "lazy-img")]').extract()[0]
            list_info_title = list_info.xpath('.//div[contains(@class, "lazy-img")]/img/@alt').extract()[0]
            print('标题：', list_info_title)
            list_info_fenshu = list_info.xpath('.//div[@class="pts"]//div/text()').extract()[0]
            print('评分：', list_info_fenshu)
            list_info_cishu = list_info.xpath('.//div[@class="detail"]/span[1]/text()').extract()[0]
            print('观看次数：', list_info_cishu)
            list_info_pinglunshu = list_info.xpath('.//div[@class="detail"]/span[2]/text()').extract()[0]
            print('评论数：', list_info_pinglunshu)
            # list_info_user = list_info.xpath('.//div[@class="detail"]//a').extract()
            print('发布者：', list_info_user)
            print('-----'*70)
            item = BilibilispriderItem()
            item['list_info_no'] = list_info_no
            item['list_info_url'] = list_info_url
            item['list_info_img_url'] = list_info_img_url
            item['list_info_title'] = list_info_title
            item['list_info_fenshu'] = list_info_fenshu
            item['list_info_cishu'] = list_info_cishu
            item['list_info_pinglunshu'] = list_info_pinglunshu
            item['list_info_user'] = list_info_user
            yield item
