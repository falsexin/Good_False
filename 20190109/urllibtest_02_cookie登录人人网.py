"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/17'
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
from urllib import request
from urllib import parse
import chardet

# _o ：去掉
Request_URL="http://www.renren.com/966924492"
head = {}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'
head['Cookie']='anonymid=jhsxb2breoia7; _r01_=1; ln_uact=17752558702; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; depovince=HEN; jebe_key=bbeaa27f-d9ca-4b24-84bb-7c1a63164ca5%7C077a3e2b1c00096d5c13732ceee74ce5%7C1537971338639%7C1%7C1537971339459; JSESSIONID=abcAxKyNVFTObczicfzyw; ick_login=ef27c59c-1d96-4ef3-830f-7e1b76a94701; first_login_flag=1; wp_fold=0; jebecookies=b55c3d38-9a71-41af-9eaf-74951c73e059|||||; _de=32B20555AD3784A6BF2D3D01B72FE013; p=291a2bb01024c67599d146e48258840c2; t=06fc3029dab408f513b4301dbf90f57a2; societyguester=06fc3029dab408f513b4301dbf90f57a2; id=966924492; xnsid=e6de3a70; ver=7.0; loginfrom=null'

#定义request对象
req = request.Request(Request_URL,headers=head)
#用post方法进行请求，指定data参数
response = request.urlopen(req)
html = response.read()
charset = chardet.detect(html)['encoding']
html = html.decode(charset)
print(html)

