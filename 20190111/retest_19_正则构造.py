import re
pattern = re.compile(r'a(?=\d)')
matchObj = pattern.match('ba123',1)
print(matchObj.group())

pattern = re.compile(r'(?<=\d)a')
matchObj = pattern.match('2a')
print(matchObj)