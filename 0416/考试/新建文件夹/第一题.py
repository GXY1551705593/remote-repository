'''说说你对Python拷贝的了解以及需要注意的地方，并用代码实现list a的拷贝, a=[1,2,3]'''
#直接赋值
# list_a=[1,2,3]
# list_b=list_a
# print(id(list_b))
# print(id(list_a))
#浅拷贝
# list_a=[1,2,3]
# list_a.append(4)
# list_b=list_a.copy()
# print(list_a)
# print(list_b)
# print(id(list_b))
# print(id(list_a))
#深拷贝
list_a=[1,2,3]
list_b=list_a
#list_a.append(4)
list_a.deepcopy()
print(list_a)
# print(list_b)
# print(id(list_b))
print(id(list_a))