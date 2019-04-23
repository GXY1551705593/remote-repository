'''说说你对Python拷贝的了解以及需要注意的地方，并用代码实现list a的拷贝, a=[1,2,3]'''
#直接赋值
#浅拷贝
#深拷贝
'''直接赋值：其实就是对象的引用（别名）。

浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。

深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。'''
# import copy
# list_a=[1,2,3,['a','b']]
# list_b=list_a
# list_c=copy.copy(list_a)
# list_d=copy.deepcopy(list_a)
# list_a.append('c')
# print(list_a)
# print(list_b)
# print(list_c)
# print(list_d)
# print(id(list_a))
# print(id(list_b))
# print(id(list_c))
# print(id(list_d))
#
#
for i in range(1,1):
    print(i)