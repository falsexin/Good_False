"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/14'
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
import time

url='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=2.def.0.V16&wq=%E6%89%8B%E6%9C%BA&pvid=8d5f606e5f7348c1bd8edb0480ba6ff6'
driver = webdriver.Chrome()
driver.get(url)

# 模拟下滑到底部的操作
for i in range(5):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)

#goods_info = driver.find_elements_by_css_selector('.gl-item')
#goods_info = driver.find_elements_by_xpath('//li[@class="gl-item"]')
goods_info = driver.find_elements_by_class_name('gl-item')
print(len(goods_info))

for info in goods_info:
    title = info.find_element_by_css_selector(".p-name.p-name-type-2 a").text.strip()
    print('title:',title)
    price = info.find_element_by_css_selector('.p-price').text.strip()
    print('price:',price)

time.sleep(2)
driver.close()