#
# @Time    : 2019/1/14 19:07
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 斗鱼热度.py
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
driver.get("https://www.douyu.com/directory/all")
for i in range(5):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
# print(len(list))
# 模拟下滑到底部的操作

for info in list:
    title = info.find_element_by_xpath('.//h3[@class="ellipsis"]').text.strip()
    print('标题:', title)
    fenglei = info.find_element_by_xpath('.//span[contains(@class,"tag ellipsis")]').text.strip()
    print('分类:', fenglei)
    name = info.find_element_by_xpath('.//span[contains(@class,"dy-name ellipsis fl")]').text.strip()
    print('主播名:', name)
    redu = info.find_element_by_xpath('.//span[contains(@class,"dy-num fr")]').text.strip()
    print('热度人气:', redu)
    print('#'*30)










