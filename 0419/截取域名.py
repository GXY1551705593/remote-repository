# '''截取域名'''
import re
# line=b'Host: localhost:8080'
#
# ret = re.match('..+Host.{10,}', str(line))
# print('这是我的域名：',ret.group()[7:-1])

while True:
    word = input('输入内容：')
    try:
        ret=re.match('[\w]{1,}',word)
        print('已匹配到:',ret.group())
    except:
        print('\w','未匹配到')
        ret1= re.match('[\W]{1,}', word)
        print('已匹配到:', ret1.group())
