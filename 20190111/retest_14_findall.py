"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/14'
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
import re
# pattern = re.compile(r'\d+')   # 查找数字
#
# result1 = pattern.findall('hello 123456.789')
# result2 = pattern.findall('one1two2three3four4', 0, 10)
# result3 = pattern.findall('one1two2three3four4')
#
# print(result1)
# print(result2)
# print(result3)

a = """<div class="el">ssad
                        <p class="t1 ">
                            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
                            <input class="checkbox" type="checkbox" name="delivery_jobid" value="101466208" jt="0" style="display:none">
                            <span>
                                <a target="_blank" title="Python教研经理" href="https://jobs.51job.com/shanghai-xhq/101466208.html?s=01&amp;t=0" onmousedown="">
                                    Python教研经理                                </a>
                            </span>
                                                                                </p>
                        <span class="t2"><a target="_blank" title="妙小程" href="https://jobs.51job.com/all/co4809293.html">妙小程</a></span>
                        <span class="t3">上海-徐汇区</span>
                        <span class="t4">1.5-2万/月</span>
                        <span class="t5">01-18</span>
                    </div>"""
a = a.replace('\n', '')
a = re.sub('\s', '', a)
print(a)
b = re.findall(r'name="(.*?)"', a)
print(b)

# a = 'dasd11.sfa.s'
#
# b = re.search(r'(?:\d+)\..*',a)
# print(b.group())

