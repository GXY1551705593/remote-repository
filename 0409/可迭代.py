'''自定义可迭代对象的实现'''
from collections import Iterable
class MyList(object):
    def __init__(self):
        self.items=list()
    #增加元素的功能
    def append_item(self,obj):
        self.items.append(obj)
   #添加__iter__这个魔方方法，使对象可以迭代
    def __iter__(self):#使写出来对象能可迭代
        return self

list_my=MyList()
list_my.append_item('java')
list_my.append_item('python')
list_my.append_item('c++')
ret=[i for i in list_my.items]
print(ret)

# list_my.append_item('python')
# list_my.append_item('c++')
# for i in list_my:
#     print(i)
# print(list_my)
# print(id(list_my))
# ret=isinstance(list_my,Iterable)
# print(ret)
