import chardet
str='helio'.encode('gbk')

print(chardet.detect(str))
