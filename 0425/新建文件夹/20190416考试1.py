# 说说你对Python拷贝的了解以及需要注意的地方，并用代码实现list a的拷贝, a=[1,2,3]


#拷贝就是把一个列表的消息都打印出来，并且不影响原来的列表
#注意点：切记不能改变原来的列表

a=[1,2,3]
new_list = a
for new_list2 in a:
    print(new_list2)