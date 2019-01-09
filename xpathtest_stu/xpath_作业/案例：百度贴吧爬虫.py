"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/8'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from urllib import request
from urllib import parse
from lxml import etree
import csv
import codecs


def tiebaSpider(url, startPage, endPage, name):
    '''
    作用：负责处理url，请求每个url，把爬取的页面数据保存。html

    :param url:
    :param startPage:
    :param endPage:
    :return:
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    barname = name
    for page in range(startPage, endPage + 1):
        pn = (page - 1) * 50
        fullurl = url + "&pn=" + str(pn)
        # 请求指定的页面
        print('请求页面，页码是：', page)
        req = request.Request(fullurl, headers=headers)
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print("存储页面内容。。。")
        # filename = 'data/第' + str(page) + "页.html"
        # with open(filename, 'w', encoding='utf-8') as file:
        #     file.write(html)
        # 数据提取
        selector = etree.HTML(html)
        ls = selector.xpath('//li[contains(@class,"j_thread_list clearfix")]')
        print('ls len:', len(ls))
        base_url = 'https://tieba.baidu.com'
        for link in ls:
            title = link.xpath('.//div[contains(@class,"threadlist_title pull_left j_th_tit")]/a/text()')[0]
            print('title:', title)
            url = base_url + link.xpath('.//div[contains(@class,"threadlist_title pull_left j_th_tit")]/a/@href')[0]
            print('url:', url)
            author = link.xpath('.//span[@class="frs-author-name-wrap"]/a/text()')[0]
            print('author:', author)
            reviw = link.xpath('.//span[@class="threadlist_rep_num center_text"]/text()')[0]
            print('reviw:', reviw)
            picture = link.xpath('.//div[@class="small_list_gallery"]/ul/li/a/img')
            for i in picture:
                print('sss:', i.get('bpic'))
                url = i.get('bpic')
                headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
                req = request.Request(url, headers=headers)
                repsonse = request.urlopen(req)
                with open('images/img_'+i.get('attr') +'.jpg', 'wb') as file:
                    file.write(repsonse.read())
            # print('picture:', picture)
            # filename = 'data/tieba_' + barname + '.txt'
            # with open(filename,'a',encoding='utf-8') as file:
            #     file.write('title:'+title+'\n'+'url:'+url+'\n'+"author:"+author)
            #     file.write('\n'+'=' * 60+'\n')
            print('=' * 60)
            #
            # filename = 'data/tieba_' + barname + '.csv'
            # with codecs.open(filename,'a',encoding='utf-8') as file:
            #     wr = csv.writer(file)
            #     wr.writerow([title,author,url])


if __name__ == '__main__':
    tiebaname = input('请输入贴吧名称：')
    startPage = int(input('请输入起始页码：'))
    endPage = int(input('请输入终止的页码：'))

    url = 'https://tieba.baidu.com/f?'
    kw = {'kw':tiebaname}
    kw = parse.urlencode(kw)
    print(kw)
    url = url + kw
    print(url)
    tiebaSpider(url,startPage,endPage,tiebaname)






