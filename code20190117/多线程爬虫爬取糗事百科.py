#
# @Time    : 2019/1/17 20:10
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 多线程爬虫爬取糗事百科.py
# @Software: PyCharm
#  ......................我佛慈悲......................
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -卍-|||||- \
#                |   | \\\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
# ..................佛祖开光 ,永无BUG...................
# ..................佛祖保佑，永不加班...................


import threading
import csv
import codecs
import time
import os
from urllib import request
from urllib import parse
from lxml import etree

class myThread(threading.Thread):  # 线程处理函数

    def __init__(self, name):
        threading.Thread.__init__(self)  # 线程类必须的初始化
        self.thread_name = name  # 将传递过来的name构造到类中的name
        self.thread_page_list = []
    def page(self, page):
        # self.thread_page = page
        self.thread_page_list.append(page)
    def run(self):
        try:
            url = 'https://www.qiushibaike.com/8hr/page/'
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
            if self.thread_name == '线程1':
                headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
            if self.thread_name == '线程2':
                headers = {'User-Agent': 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11'}
            if self.thread_name == '线程3':
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'}
            # print('*****'*30)
            for page in self.thread_page_list:
                # print("%s爬取了第%s页" % (self.thread_name, page))
                fullurl = url + str(page)
                # 请求指定的页面
                # print('请求页面，页码是：', page)
                # print(fullurl)
                req = request.Request(fullurl, headers=headers)
                print(1)
                response = request.urlopen(req)
                html = response.read()
                # print("存储页面内容。。。")
                filename = 'data/百科第' + str(page) + "页.html"
                # with open(filename, 'wb') as file:
                #     file.write(html)
                # 数据提取
                selector = etree.HTML(html)
                ls = selector.xpath('//li[contains(@id,"qiushi_tag")]')
                # print('ls len:', len(ls))
                base_url = 'https://www.qiushibaike.com'
                base_url1 = 'http:'
                for link in ls:
                    title = link.xpath('.//a[contains(@class,"recmd-content")]/text()')
                    # print('title:', ''.join(title).strip())
                    url2 = base_url + link.xpath('.//a[contains(@class,"recmd-content")]/@href')[0]
                    # print('url:', url2)
                    req = request.Request(url2, headers=headers)
                    repsonse = request.urlopen(req)
                    html = repsonse.read()
                    selector = etree.HTML(html)
                    neititle = selector.xpath('//h1[@class="article-title"]/text()')[0]
                    # print('标题：', ''.join(neititle).strip())
                    #
                    neirong = selector.xpath('//div[@class="content"]/text()')
                    # print('内容：', neirong)

                    neitupian = selector.xpath('//div[@class="thumb"]/img/@src')
                    if not os.path.exists('./images/baike/'):
                        os.makedirs('./images/baike/')
                    for i in neitupian:
                        # print('图片：', base_url1 + i)
                        req = request.Request(base_url1 + i, headers=headers)

                        # repsonse = request.urlopen(req)
                    #     with open('./images/baike/img_第' + str(page) + '页' + str(time.time()) + '.jpg', 'wb') as file:
                    #         file.write(repsonse.read())
                    # # neishipin = selector.xpath('//video[@id="article-video"]/source/@src')
                    #
                    # for i in neishipin:
                    #     # print('视频：', i)
                    #     req = request.Request(i, headers=headers)
                    #     repsonse = request.urlopen(req)
                    #     with open('./images/baike/vido_' + str(time.time()) + '.mp4', 'wb') as file:
                    #             file.write(repsonse.read())

                    # author = link.xpath('.//span[@class="recmd-name"]/text()')[0]
                    # print('author:', author)
                    # reviw = link.xpath('.//div[@class="recmd-num"]/span[4]/text()')
                    # print('评论:', reviw)
                    # dianzan = link.xpath('.//div[@class="recmd-num"]/span[1]/text()')[0]
                    # print('点赞数:', dianzan)
                    # picture = link.xpath('.//a[contains(@class,"recmd-left")]/img/@src')[0]
                    # print('picture:', base_url + picture)
                    #
                    # url1 = base_url1 + picture
                    # headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
                    # req = request.Request(url1, headers=headers)
                    # repsonse = request.urlopen(req)
                    # with open('images/百科_img_'+ author+title[0:2] +'.jpg', 'wb') as file:
                    #     file.write(repsonse.read())

                    #     for i in picture:
                    #         print('sss:', i.get('bpic'))
                    #         url = i.get('bpic')
                    #         headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
                    #         req = request.Request(url, headers=headers)
                    #         repsonse = request.urlopen(req)
                    #         with open('images/img_'+i.get('attr') +'.jpg', 'wb') as file:
                    #             file.write(repsonse.read())

                    # filename = 'data/百科.txt'
                    # with open(filename,'a',encoding='utf-8') as file:
                    #     file.write('title:'+str(title)+'\n'+'url:'+url2+'\n'+"author:"+author+'\n'+"reviw:"+str(reviw)+'\n'+"dianzan:"+dianzan)
                    #     file.write('\n'+'=' * 60+'\n')
                    # print('=' * 60)
            # print('*****' * 30)
            print(self.thread_name + '完成')
        except:
            print(self.thread_name + '出错')




startPage = int(input('请输入起始页码：'))
endPage = int(input('请输入终止的页码：'))
thread1 = myThread("线程1")
thread2 = myThread("线程2")
thread3 = myThread("线程3")
for i in range(startPage, endPage+1, 3):
    if i <  endPage+1:
        thread1.page(i)
    if i + 1 <  endPage+1:
        thread2.page(i+1)
    if i + 2 <  endPage+1:
        thread3.page(i+2)
# 开启线程
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
# # 等到线程1、2、3、4结束才进行以下的代码（同步）
# thread1.join()
# thread2.join()
# thread3.join()

