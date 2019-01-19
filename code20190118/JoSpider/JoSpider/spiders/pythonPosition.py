# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import JospiderItem

class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'
    allowed_domains = ['51job.com']

    def __init__(self):
        self.city = 10000
        self.max_city = 40000
        self.page = 1
        self.max_pages = 3
        self.str1 = 'https://search.51job.com/list/0'
        self.str2 = ',000000,0000,00,9,99,python,2,'
        self.str3 = '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def get_url(self):
        return self.str1 + str(self.city) + self.str2 + str(self.page) + self.str3

    def parse(self, response):

        job_list = response.xpath("//div[@class='dw_table']/div[@class='el']")
        for each in job_list:
            name = each.xpath(".//p[contains(@class,'t1 ')]//a/text()").extract()[0].strip()
            print(name)
            gs_name = each.xpath("./span[@class='t2']/a/text()").extract()[0]
            print('公司名：', gs_name)
            city = each.xpath("./span[@class='t3']/text()").extract()[0]
            print('工作地点：',city)
            pub_date = each.xpath(".//span[@class='t5']/text()").extract()[0]
            print('发布日期：', pub_date)
            salary = each.xpath(".//span[@class='t4']/text()").extract()
            if len(salary) > 0:
                salary = salary[0]
                salary = salary[:salary.index('/')]
            else:
                salary = '面议/无'
            print('薪资：', salary)
            print('-----'*40)
            item = JospiderItem()
            item['name'] = name
            item['gs_name'] = gs_name
            item['city'] = city
            item['pub_date'] = pub_date
            item['salary'] = salary
            yield item

            # 翻页的处理
            # 从当前的url中提取当前的城市
            p = self.str1 + r'(\d+).*?'
            currcity = re.search(p, response.url).group(1)
            # 从当前的url中提取当前的页码
            p = self.str1 + currcity + self.str2 + r'(\d+).*?'
            curpage = re.search(p, response.url).group(1)
            self.page = int(curpage) + 1
            print('curpage:', curpage)
            print('curcity:', currcity)
            if self.page <= self.max_pages:
                url = self.get_url()
                print('new page:', url)
                # 发送新的url，加入对列，等待爬取；指定回调函数处理响应对象
                yield scrapy.Request(url, callback=self.parse)
            else:
                self.city = int(currcity) + 10000
                if self.city <= self.max_city:
                    self.page = 1
                    url = self.get_url()
                    print('new city url:', url)
                    yield scrapy.Request(url, callback=self.parse)