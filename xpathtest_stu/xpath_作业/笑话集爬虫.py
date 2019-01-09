#
# @Time    : 2019/1/8 19:31
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 笑话集爬虫.py
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


def xiaohuaSpider(url, startPage, endPage):
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
        # print("存储页面内容。。。")
        # filename = 'data/笑话集第' + str(page) + "页.html"
        # with open(filename, 'wb') as file:
        #     file.write(html)
        # # 数据提取
        selector = etree.HTML(html)
        ls = selector.xpath('//div[@align="center"]//tr[@valign="top"]//table[@width=646]')
        print('ls len:', len(ls))
        base_url = 'http://www.jokeji.cn'
        for link in ls:
            title = link.xpath('.//a[contains(@class,"main_14")]/text()')[0]
            print('title:', title)
            url1 =link.xpath('.//a[contains(@class,"main_14")]/@href')[0]
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

            url1 = parse.quote(url1)
            url1 = base_url + url1
            req = request.Request(url1, headers=headers)
            repsonse = request.urlopen(req)
            html = repsonse.read()
            selector = etree.HTML(html)
            ls = selector.xpath('//span[@id="text110"]//p/text() | //span[@id="text110"]//p//font/text()')
            # print(len(ls), ls)
            print('url:', url1)
            liulan = link.xpath('.//td[@width=124]/text()')[0]
            print(liulan)
            data = link.xpath('.//span[@class="date"]/text()')
            print('日期:', ''.join(data).strip())
            neirong = ''
            for i in ls:
                # print(i.encode('utf-8').decode('utf-8'))
                neirong += i.encode('utf-8').decode('utf-8') + '\n'
            print('笑话内容：',neirong)
            filename = 'data/笑话集_第'+ str(page) +'页.txt'
            with open(filename,'a',encoding='utf-8') as file:
                file.write('title:'+str(title)+'\n'+'url:'+url1+'\n'+liulan+'\n'+"日期:"+''.join(data).strip()+'\n'+"笑话内容:"+neirong)
                file.write('\n'+'=' * 60+'\n')
        #     dianzan = link.xpath('.//div[@class="recmd-num"]/span[1]/text()')[0]
        #     print('点赞数:', dianzan)
        #
        #     picture = link.xpath('.//a[contains(@class,"recmd-left")]/img/@src')[0]
        #     print('picture:', base_url+picture)
        #     url1 = base_url+picture
        #     headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
        #     req = request.Request(url1, headers=headers)
        #     repsonse = request.urlopen(req)
        #     with open('images/百科_img_'+ author+title[0:2] +'.jpg', 'wb') as file:
        #         file.write(repsonse.read())
        #     print('picture:', picture)

            print('=' * 60)
        #     #
        #     filename = 'data/百科.csv'
        #     with codecs.open(filename,'a',encoding='utf-8') as file:
        #         wr = csv.writer(file)
        #         wr.writerow([title,author,url1,reviw,dianzan])


if __name__ == '__main__':
    startPage = int(input('请输入起始页码：'))
    endPage = int(input('请输入终止的页码：'))

    url = 'http://www.jokeji.cn/hot.asp?me_page='
    # print(url)
    xiaohuaSpider(url,startPage,endPage)



