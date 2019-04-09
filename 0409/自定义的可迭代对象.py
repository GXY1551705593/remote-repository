'''这是自定义可迭代对象的实现'''
from collections import Iterable
class MyList:
    def __init__(self):
        self.items = list()

    # 增加元素的功能
    def append_item(self,obj):
        self.items.append(obj)
     # 添加__iter__这个魔法方法，表示对象那个可以迭代


    def __iter__(self):
        pass

mylist = MyList()
mylist.append_item(3)
mylist.append_item(2)
print(mylist)
ret = isinstance(mylist,Iterable)
print('判断mylist是否可以被迭代',ret)
# for i in mylist:
#     print(i)
