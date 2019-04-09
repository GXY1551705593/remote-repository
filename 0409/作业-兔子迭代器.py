'''用迭代器写生兔子'''
from collections import Iterator#引入迭代器包
class Rabbit_Iterator(object):#创建类来完成用迭代器写兔子
    def __init__(self):
        pass
    '''append_month()方法用来写兔子'''
    def append_month(self,month):
        if 0<month<3:
            month=1
            print(month)
            ret1=isinstance(iter([month]),Iterator)
            print(ret1)
        else:
            month=(month-1)+(month-2)
            print(month)
            ret2= isinstance(iter([month]), Iterator)
            print(ret2)
    '''用__iter__方法，'''
    def __iter__(self):
        pass
eg=Rabbit_Iterator()
eg.append_month(5)