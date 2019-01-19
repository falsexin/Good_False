"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/15'
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
from selenium import webdriver
import random
import time

loginname = '3414018462@qq.com'
password='qikuedu9527'

def login():
    '''
    登录微博
    :return:
    '''
    driver = webdriver.Chrome()
    try:
        driver.set_window_size(1124,850)
        print('开始登录微博....')
        driver.get('http://www.weibo.com/login.php')
        time.sleep(2)
        print('输入用户名...')
        driver.find_element_by_id('loginname').clear()
        driver.find_element_by_id('loginname').send_keys(loginname)
        time.sleep(2)
        print('输入密码...')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(password)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
        print('登录....')
        time.sleep(3)
        return driver
    except Exception as e:
        print('登录失败')
        print(e)


def weiboSpider(driver,url):
    '''
    爬取指定微博的数据
    :param driver:
    :param url:
    :return:
    '''
    try:
        print('进入指定微博....')
        driver.set_window_size(1124, 850)
        driver.get(url)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            print('页面加载中....')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.random()*10)
            new_height  = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break;
            last_height = new_height

    except Exception as e:
        print('加载失败',e)

    # 微博数据的提取
    ls = driver.find_elements_by_xpath('//div[@class="WB_detail"]')
    print(len(ls))
    for item in ls:
        name = item.find_element_by_xpath('.//div[@class="WB_info"]/a').text
        print(name)
        pub_date=item.find_element_by_xpath('.//div[@class="WB_from S_txt2"]/a').text
        print(pub_date)
        content = item.find_elements_by_xpath('.//div[@class="WB_text W_f14"]')
        if len(content)>0:
            content = content[0].text.strip()
        else:
            content='空'
        print(content)
        print('='*60)

if __name__ == "__main__":
    id = input('请输入微博id：')
    url = 'https://weibo.com/'+ id +'?is_all=1'
    print(url)
    driver = login()
    weiboSpider(driver,url)


