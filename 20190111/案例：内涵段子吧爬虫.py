"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/12'
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
import re
import requests
from urllib import request

if __name__ == '__main__':
    url = 'https://www.neihan8.com/article/index.html'
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    # print(html)
    # 数据提取
    # 定义匹配条目的对象
    pat_item = re.compile(
        r'<div class="text-column-item box box-790">(.*?<div class="view".*?)</div>.*?</div>.*?</div>', re.S)
    item_ls = pat_item.findall(html)
    pat_title = re.compile(r'class="title".*?>(.*?)</a>', re.S | re.M)
    pat_url = re.compile(r'<h3><a href="(.*?)"', re.S | re.M)
    pat_support = re.compile(r'<div class="good".*?>(.*?)</div>', re.S | re.M)
    pat_aginst = re.compile(r'<div class="bad".*?>(.*?)</div>', re.S | re.M)
    pat_content = re.compile(r'<div class="detail">.*?</div>.*?</div>.*?</div>(.*)<div class="ad610">', re.S | re.M)
    print(item_ls)
    print(len(item_ls))
    for item in item_ls:
        title = pat_title.search(item).group(1)
        print("title:", title)
        detail_url = 'https://www.neihan8.com' + pat_url.search(item).group(1)
        print('detail_url:', detail_url)
        support_nums = pat_support.search(item).group(1)
        print('support nums:', support_nums)
        against_nums = pat_aginst.search(item).group(1)
        print("against nums:", against_nums)
        response = requests.get(detail_url, headers=headers)
        html2 = response.content.decode()
        # print(html2)
        content = pat_content.search(html2)
        if content != None:
            content = content.group(1)
        else:
            content = '空'
        print('content:', content)
        print('=' * 60)
