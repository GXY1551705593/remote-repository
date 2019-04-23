import re
result='hello world,哈喽'
ret=re.findall('world|哈喽',result)
print(ret)
# import re
# result='hello world,哈喽'
# ret=re.search('world',result)
# print(ret.group())