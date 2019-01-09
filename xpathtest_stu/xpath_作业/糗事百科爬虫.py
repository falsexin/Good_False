#
# @Time    : 2019/1/8 17:39
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 糗事百科爬虫.py
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


from urllib import request
from urllib import parse
from lxml import etree
import csv
import codecs
import time


def baikeSpider(url, startPage, endPage):
    '''
    作用：负责处理url，请求每个url，把爬取的页面数据保存。html

    :param url:
    :param startPage:
    :param endPage:
    :return:
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    for page in range(startPage, endPage + 1):
        fullurl = url + str(page)
        # 请求指定的页面
        print('请求页面，页码是：', page)
        print(fullurl)
        req = request.Request(fullurl, headers=headers)
        response = request.urlopen(req)
        html = response.read()
        print("存储页面内容。。。")
        filename = 'data/百科第' + str(page) + "页.html"
        # with open(filename, 'wb') as file:
        #     file.write(html)
        # 数据提取
        selector = etree.HTML(html)
        ls = selector.xpath('//li[contains(@id,"qiushi_tag")]')
        print('ls len:', len(ls))
        base_url = 'https://www.qiushibaike.com'
        base_url1 = 'http:'
        for link in ls:
            title = link.xpath('.//a[contains(@class,"recmd-content")]/text()')
            print('title:', ''.join(title).strip())
            url2 = base_url + link.xpath('.//a[contains(@class,"recmd-content")]/@href')[0]
            print('url:', url2)
            req = request.Request(url2, headers=headers)
            repsonse = request.urlopen(req)
            html = repsonse.read()
            selector = etree.HTML(html)
            neititle = selector.xpath('//h1[@class="article-title"]/text()')[0]
            print('标题：', ''.join(neititle).strip())

            neirong = selector.xpath('//div[@class="content"]/text()')
            print('内容：', neirong)

            neitupian = selector.xpath('//div[@class="thumb"]/img/@src')
            for i in neitupian:
                print('图片：', base_url1+i)
                req = request.Request(base_url1+i, headers=headers)
                repsonse = request.urlopen(req)
                with open('images/baike/img_' + str(time.time())+ '.jpg', 'wb') as file:
                        file.write(repsonse.read())
            neishipin = selector.xpath('//video[@id="article-video"]/source/@src')

            for i in neishipin:
                print('视频：', i)
                req = request.Request(i, headers=headers)
                repsonse = request.urlopen(req)
                with open('images/baike/vido_' + str(time.time()) + '.mp4', 'wb') as file:
                        file.write(repsonse.read())

            author = link.xpath('.//span[@class="recmd-name"]/text()')[0]
            print('author:', author)
            reviw = link.xpath('.//div[@class="recmd-num"]/span[4]/text()')
            print('评论:', reviw)
            dianzan = link.xpath('.//div[@class="recmd-num"]/span[1]/text()')[0]
            print('点赞数:', dianzan)
            picture = link.xpath('.//a[contains(@class,"recmd-left")]/img/@src')[0]
            print('picture:', base_url+picture)

            url1 = base_url1+picture
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
            req = request.Request(url1, headers=headers)
            repsonse = request.urlopen(req)
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
            print('=' * 60)
            # #
            # filename = 'data/百科.csv'
            # with codecs.open(filename,'a',encoding='utf-8') as file:
            #     wr = csv.writer(file)
            #     wr.writerow([title,author,url1,reviw,dianzan])


if __name__ == '__main__':
    startPage = int(input('请输入起始页码：'))
    endPage = int(input('请输入终止的页码：'))

    url = 'https://www.qiushibaike.com/8hr/page/'
    # print(url)
    baikeSpider(url,startPage,endPage)





