#
# @Time    : 2019/1/14 16:51
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 京东搜索后爬虫.py
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

# 导入 webdriver
from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time

def jd_seach(seach_zifu):
    driver = webdriver.Chrome()
    driver.get("https://www.jd.com/")
    time.sleep(2)
    input_search = driver.find_element_by_xpath('//div[@id="J_searchbg"]//following-sibling::*[1]')
    input_search.send_keys(seach_zifu)
    input_sumbit = driver.find_element_by_xpath('//button[@clstag="h|keycount|head|search_c"]')
    # print(len(input_sumbit))

    input_sumbit.click()
    print(driver.window_handles)
    driver.switch_to_window(driver.window_handles[0])

    # 模拟下滑到底部的操作
    for i in range(5):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)

    # driver.switch_to_window(driver.window_handles)
    goods_info = driver.find_elements_by_css_selector('.gl-item')
    print(driver.current_url)
    print(len(goods_info))
    for info in goods_info:
        title = info.find_element_by_css_selector(".p-name.p-name-type-2 a").text.strip()
        print('title:', title)
        price = info.find_element_by_css_selector('.p-price').text.strip()
        print('price:', price)

if __name__ == '__main__':
    seach_zifu = input('请输入搜索的字符：')
    jd_seach(seach_zifu)









