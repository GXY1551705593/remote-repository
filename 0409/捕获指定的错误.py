'''发生错误，进入except没有错误进入else无论有没有错误，一定要进finally'''
try:
    print('正确')
except (IOError,NameError):
    print('错误')
else:
    print('—else—')
finally:
    print('——finally——')