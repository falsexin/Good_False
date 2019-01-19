#
# @Time    : 2019/1/16 17:56
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 海报.py
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

import requests
import time
import json
import os
import urllib
from lxml import etree
from datetime import datetime
from urllib import parse

# datime =  time.gmtime()
# print(datime)
# a = time.strftime('%Y-%y-%m-%d-%H-%I-%M-%S-%a-%A-%b-%B-%c-%j-%p-%U-%w-%W-%x-%X-%Z', datime)
# print(a)
#
# dt=datetime.now()
# t=dt.strftime('%a %b %d %Y %X')
# print(t)
# %a %b %d %Y %X GMT 0800
# stamp: Wed Jan 16 2019 17:50:14 GMT 0800 (中国标准时间)

def   haibao(i):
    temp = 0
    for t in range(i):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,\
            like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Referer": "http://pic.haibao.com",
            "Cookie": "hbUnregUserId=0CD847A3-DFE5-4888-A53B-527A6AE392E6; Hm_lvt_793a7d1dd685f0ec4bd2b50e47f13a15=1547631528; Hm_lvt_9448a813e61ee0a7a19c41713774f842=1547631532; Hm_lvt_06ffaa048d29179add59c40fd5ca41f0=1547631535; Hm_lpvt_9448a813e61ee0a7a19c41713774f842=1547640283; Hm_lpvt_06ffaa048d29179add59c40fd5ca41f0=1547640293; Hm_lpvt_793a7d1dd685f0ec4bd2b50e47f13a15=1547640294"
        }

        word = parse.urlencode({"stamp": datetime.now().strftime('%a %b %d %Y %X') + 'GMT 0800 (中国标准时间)'})
        base_url = 'http://pic.haibao.com/ajax/image:getHotImageList.json?'

        Form_Data = {
            'skip': temp
        }
        response = requests.post(base_url + word, data=Form_Data, headers=headers)
        # print(response.text)
        if response.status_code == 200:
            data = json.loads(response.text)
            html = ''.join(data['result']['html'].replace(r'\t', '').replace(r'\r', '').replace(r'\n', '')).strip()
            selector = etree.HTML(html)
            picture = selector.xpath('//div[contains(@class,"pageli jsImageContainer jsImageInfo ")]')
            temp_1 = len(picture)
            # print(len(picture))
            for info in picture:
                picture_path = info.xpath('.//div[contains(@class, "pagelibox")]//img/@data-original')
                picture_path = str(picture_path[0])
                print('图片地址：', picture_path)
                response1 = requests.get(picture_path)
                with open('images/海报/img_' + str(time.time()) + '.jpg', 'wb') as file:
                    file.write(response1.content)

            # print('----'*30)
        temp += temp_1

if __name__ == '__main__':
    i = int(input('请输入你要获取图片要加载的次数:'))
    if not os.path.exists('./images/海报'):
        os.makedirs('./images/海报')
    haibao(i)