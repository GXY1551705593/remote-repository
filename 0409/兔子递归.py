from collections import Iterator#import 导入迭代器包
def rabbit(month):#定义函数rabbit
    '''用递归方法求兔子数量'''
    if 0<month<3:
        month=1
        yield month#yield 的作用就是把一个函数变成一个 generator
    else:
        month=(month-1)+(month-2)
        yield month
ret=rabbit(4)
ret2=isinstance(ret,Iterator)
print(ret2)
print(next(ret))
