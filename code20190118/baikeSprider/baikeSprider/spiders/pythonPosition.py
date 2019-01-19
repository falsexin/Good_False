# -*- coding: utf-8 -*-
import scrapy
import re

class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    # allowed_domains = ['qiushibaike.com']
    # start_urls = ['https://www.qiushibaike.com/8hr/page/1/']
    allowed_domains = ['51job.com']
    start_urls = [
        'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        # print(response.body)
        print('ssssssssss', dir(response))
        # job_list = response.xpath("//div[@class='dw_table']/div[@class='el']")
        # pat = r'(?<=<title>).*?(?=</title>)'
        # a = r'(?<=<div class="el">).*?(?<=</div>)'
        # ex = re.compile(a, re.M | re.S)
        # job_list = response.selector.re.findall(ex, )

        print(len(response.selector.re(r'(?<=<div\s*).*?(?<=</div>)', re.M | re.S) ))
