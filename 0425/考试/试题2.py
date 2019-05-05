'''在下面函数中，写出print对应的值，分析为什么会出现这个结果？对该代码的修改有什么建议？
def fn(a=[]):
    a.append(1)
    return a
b = fn([1, 2, 3])
print b
c = fn()
print c
d = fn()
print c
print d'''
def fn(a=[]):
    a.append(1)
    return a
b = fn([1, 2, 3])
print(b)
c = fn()
print(c)
d = fn()
print(c)
print(d)

'''该代码原先print使用的是python2的写法，应加上（）修改为python3的写法
print(a)的值为[]代码的操作完成末尾追加了整数1，抛出a的值1
print(b)的值为[1,2,3,1]在b的原来的列表末尾追加了a的值1
print(c)的值为[1]将a的值追加在c的结果上所以c的值为1
第二个print(c)在原先的c的值上再次追加了整数1,所以得到的结果为[1,1]
print(d)的值为[1,1]由于它是在print(c)后打印,所以print(d)的结果和第二个print(c)的结果相同
'''
