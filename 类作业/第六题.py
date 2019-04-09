'''要求： 可以指定一批生成的个数，可以指定数值的范围，可以调整每批生成数字的个数。'''
import random
class Numbers(object):
    def __init__(self,count,start,stop):#添加指定生成的个数，可以指定数值的范围，可以调整每批生成数字的个数
        self.count=count
        self.start=start
        self.stop=stop
    def adjust(self):#给出adjust方法
        # list=[]
        # for i in range(self.count):#用for循环
        #     ret=random.randint(self.count, self.stop)
        #     list.append(ret)
        #     if len(list)==self.count:
        #         return list
        return [random.randint(self.count,self.stop) for i in range(self.count)]#用列表推导式
numbers=Numbers(5,1,50)
print(numbers.adjust())
