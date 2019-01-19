#
# @Time    : 2019/1/16 9:21
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 豆瓣.py
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
import json

def crawl(i):
    base_url = 'https://movie.douban.com/j/new_search_subjects'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,\
    like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    keywords = {
        'sort': 'U',
        'range': '0, 10',
        'tags': '搞笑',
        'start': '0',
        'genres': '喜剧',
        'countries': '中国大陆',
        'year_range': '2018, 2018'
    }

    response = requests.get(base_url, params=keywords, headers=headers )
    if response.status_code == 200:
        print(response.text)
        data = json.loads(response.text)['data']
        # print(data)
        for item in data:
            print('导演:', item['directors'])
            print('评分:', item['rate'])
            print('星级:', item['star'])
            print('标题:', item['title'])
            for t in item['casts']:
                print('主演:', t,'\t', end='')
            print('--'*40)

if __name__ == '__main__':
    for i in range(3):
        crawl(i)