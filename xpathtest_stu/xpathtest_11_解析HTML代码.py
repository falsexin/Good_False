"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/13'
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
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item"><a href="link1.html">first item</a></li>
         <li class="item"><a href="link2.html">second item</a></li>
         <li class="item"><a href="link3.html">third item</a></li>
         <li class="item"><a href="link4.html">fourth item</a></li>
         <li class="item"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
     <a href="link6.html">text</a>
     <a href="link7.html">text</a>
 </div>
'''

#利用etree.HTML，将字符串解析为HTML文档
html = etree.HTML(text)
print(type(html))
# 按字符串序列化HTML文档
print(html)
results = html.xpath('//li/a')
print(results)
for item in results:
    print(item.text)



