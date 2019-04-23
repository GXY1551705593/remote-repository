'''re正则表达式'''
import re
#.匹配任何一个字符，一 .代表一位数，加{n}替代点的数量
# ret=re.match('h.{2}l','hallo')
# try:
#     print('匹配到',ret.group())
# except:
#     print('没有匹配到')
#
ret2=re.match('[name]{3}','name')
# try:
#     print('匹配到',ret2.group())
# except:
#     print('没有匹配到')
# ret3=re.fullmatch('\w','h')
# try:
#     print('匹配到',ret3.group())
# except:
#     print('没有匹配到')
#
# list=['a','b','c']
# for line in list.items:
#     # print(line[0:4])
#     if line[0:4] == b'Host':
#         # print(line)
#         ret = re.match('Host.{10,}', str(line))
#         print('这是我的域名：', ret.group())
# for i in range(5):
#     print(i,end='+')
#     if i<i+1:
#         print('=',5)