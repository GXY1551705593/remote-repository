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
        '''需要返回的是一个迭代器'''
        myiterator = MyIterator(self.items)
        return myiterator
        pass
#



class MyIterator:
    def __init__(self,items):
        self.items = items
        self.current_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        """在当前的方法里面，实现记录位置和值"""
        if self.current_index <len(self.items):
            value = self.items[self.current_index]
            self.current_index += 1
            print(value)
        else:
            raise  StopIteration


mylist = MyList()
mylist.append_item('java')
mylist.append_item('python')
mylist.append_item('c++')
print(mylist.items)
# ret = isinstance(mylist,Iterable)
# print('判断mylist是否可以被迭代',ret
my1=MyIterator(mylist.items)
my1.__next__()
my1.__next__()
my1.__next__()