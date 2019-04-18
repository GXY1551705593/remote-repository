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
print d
'''
def fn(a=[]):
    a.append(1)
    return a
# b = fn([1, 2, 3])
# print(b)#[1, 2, 3, 1]，append(1)
c = fn()
# print(c)#[1],[]加append(1)
d = fn()
print(c)#[1, 1],又运行了一次函数得到[1]，加append(1)
print(d)#[1, 1],运行c得到[1]，加append(1)
#建议：
''' 1.命名规范化,键名直译；
    2.print要加（）；
    3.添加注释'''