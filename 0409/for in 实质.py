ret=(i for i in range(3))
'''用next()方法调用下一个元素并打印出来'''
print(next(ret))
print(next(ret))
print(next(ret))

print('##############################################')
'''用for in循环打印全部元素'''
ret1=(i for i in range(3))
for i in ret1:
    print(i)
print('##############################################')
'''用for in实质 while循环打印'''
from collections import Iterator;
ret2=(i for i in range(3))
ret3=isinstance(ret2,Iterator)
print(ret3)
while True:#循环的本质通过迭代器，最终遍历的是迭代器
    try:
        ret4=next(ret2)
        print(ret4)
    except StopIteration as e:
        break

