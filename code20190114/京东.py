#
# @Time    : 2019/1/14 14:11
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 京东.py
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
from selenium import webdriver
import time

url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=2.def.0.V03&wq=shouji&pvid=b06ab3933c78421688ec080dd5e9b9ee"
driver = webdriver.Chrome()
driver.get(url)

for i in range(5):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)

# goods_info = driver.find_elements_by_css_selector(".gl-item")
# goods_info = driver.find_elements_by_class_name('gl-item')
goods_info = driver.find_elements_by_xpath('//li[@class="gl-item"]')
print(len(goods_info))
for info in goods_info:
    title = info.find_element_by_css_selector(".p-name.p-name-type-2 a").text.strip()
    print('title:', title)
    price = info.find_element_by_css_selector('.p-price').text.strip()
    print('price:', price)


























