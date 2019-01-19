#
# @Time    : 2019/1/14 19:58
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 网易科技频道.py
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
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://tech.163.com/")
#
# for i in range(7):
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#     time.sleep(1)

list = driver.find_elements_by_xpath('//div[contains(@class,"data_row news_article clearfix")]')
for info in list:
    title = info.find_element_by_xpath('.//div[contains(@class,"news_title")]//h3//a').text.strip()
    print('标题:', title)
    url = info.find_element_by_xpath('.//div[contains(@class,"news_title")]//h3/a').get_attribute('href')
    # print(dir(url))
    print('标题:', url)
    print('#' * 30)