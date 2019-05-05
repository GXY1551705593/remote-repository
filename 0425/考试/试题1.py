'''说说你对Python拷贝的了解以及需要注意的地方，并用代码实现list a的拷贝,a=[1,2,3] '''
'''赋值拷贝'''
a=[1,2,3]
b=[]
b=a
print(b)
print(id(a))
print(id(b))
#赋值拷贝得到的结果相同，得到的地址不同


'''浅拷贝'''
a=[1,2,3]
b.copy()
print(b)
print(id(a))
print(id(b))
#浅拷贝得到地址不同，得到的结果相同

'''深拷贝'''
a=[1,2,3]
import copy
copy.deepcopy(b)
print(b)
print(id(a))
print(id(b))
#深拷贝得到的结果相同，得到的地址不同