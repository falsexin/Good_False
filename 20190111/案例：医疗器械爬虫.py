"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/11'
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
import requests
from bs4 import BeautifulSoup
import re


def down(url):
    '''
    请求页面
    :param url:
    :return:
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    response = requests.get(url, headers=headers)
    html = response.text
    return (html, response.url)


def get_cates():
    '''
    获取分类
    :return:
    '''
    url = 'http://www.chinamedevice.cn/'
    html, current_url = down(url)
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    # 提取class="type"的div下面的ul标签
    ls = soup.select('div.type > ul')
    print(len(ls))
    # 提取每一个ul标签下的h3和h2标签下的a标签
    cate_ls = []
    for item in ls:
        ls1 = item.select('h2 a')
        ls2 = item.select('h3 a')
        cate_ls.extend(ls1)
        cate_ls.extend(ls2)
    print(len(cate_ls))
    # 遍历处理每一个分类
    base_url = 'http://www.chinamedevice.cn'
    for item in cate_ls:
        cate_name = item.text
        # print(cate_name)
        cate_url = base_url + item.attrs['href']
        # print(cate_url)
        # 请求指定分类的产品列表
        get_product_list(cate_url, cate_name)


def get_product_list(cate_url, cate_name):
    '''
    根据url，获取指定分类的产品列表
    :param cate_url:
    :param cate_name:
    :return:
    '''
    html, current_url = down(cate_url)
    soup = BeautifulSoup(html, 'lxml')
    product_ls = soup.select('div.list > ul > li')
    # print(len(product_ls))

    for pitem in product_ls:
        purl = pitem.select_one('h3 > span > a').attrs['href']
        pname = pitem.select_one('h3 > span > a').get_text()
        # print('pname:',pname)
        get_product(purl)

    # 翻页处理
    next_page = soup.select('.fno')
    if len(next_page) > 0:
        if next_page[-1].get_text() == '下一页':
            next_url = next_page[-1].attrs['href']
            pat = re.compile(r'(\d+\.html)')
            next_url = pat.sub(next_url, current_url)
            print('next_page:', next_url)
            get_product_list(next_url, cate_name)


def get_product(url):
    '''
    根据指定产品的url，提取产品的信息
    :param url:
    :return:
    '''
    html, current_url = down(url)
    soup = BeautifulSoup(html, 'lxml')
    # 产品名称
    pname = soup.select_one('#main > dl > dt > h1').get_text()
    print("产品名称：", pname)
    purl = url
    print('url:', url)

    # 封面url
    cover_url = soup.select_one('.img > a > img').attrs['src']
    print('封面：', cover_url)

    item = soup.select('#main > dl > dd > div > ul > li')
    cate_name = item[1].contents[-1].strip()
    print('产品分类：', cate_name)

    en_name = item[2].select('h3')
    if len(en_name) > 0:
        if en_name[0] != None:
            en_name = en_name[0].text
    else:
        en_name = '无'
    print('英文名称：', en_name)

    number = item[3].contents[1].text.strip()
    print("批准文号：", number)

    spec = item[4]
    if len(spec) == 2:
        spec = spec.contents[1].strip()
    else:
        spec = '无'
    print('主要规格:', spec)

    descr = soup.select('.text03')
    if len(descr) > 0:
        descr = descr[0].text.strip()
    else:
        descr = '无'
    print("产品说明：", descr)

    producter = soup.select_one('li.bgwhite.pt > h3 > a').text.strip()
    print('生产企业：', producter)

    proucter_url = soup.select_one('li.bgwhite.pt > h3 > a').attrs['href']
    print("企业页面：", proucter_url)

    contacter = soup.select(".text04 > ul > li")[2].text.split('：')[-1]
    print('联系人：', contacter)

    phone = soup.select(".text04 > ul > li")[3]
    phone = phone.contents[0].strip().split('：')
    if len(phone) == 2:
        phone = phone[1]
    else:
        phone = '空'
    print('联系电话：', phone)

    mobile = soup.select(".text04 > ul > li")[5]
    mobile = mobile.contents[0].strip().split('：')
    if len(mobile) == 2:
        mobile = mobile[1]
    else:
        mobile = '空'
    print('移动电话：', mobile)

    address = soup.select(".text04 > ul > li")[9]
    address = address.contents[0].strip().split('：')
    if len(address) == 2:
        address = address[1]
    else:
        address = '空'
    print('地址：', address)
    print('=' * 60)


def save_data():
    '''
    保存提取的数据
    :return:
    '''
    pass


if __name__ == "__main__":
    get_cates()
