from urllib import request
import chardet
if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    charset = chardet.detect(html)['encoding']
    print(charset)
    html = html.decode(charset)
    print(html)