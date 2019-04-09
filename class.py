'''目的创造关于狗的类'''
class Dog(object):
    def __init__(self,name,age,color):#为狗类添加静态属性
        self.name=name
        self.age=age
        self.color=color
        self.leg=4
        '''关于狗类的一些方法操作'''
    def sport(self,style):
        if style==1:
            print('这只狗正在跑')
        else:
            print('这只狗正在跳')
    def bark(self):
        print('%s岁的%s正在大叫'%(self.age,self.name))
dog1=Dog('小黑',2,'white')
# print(dog1)
# print(id(dog1))
# print(dog1.age)
# print(dog1.color)
# print(dog1.leg)
# dog1.sport(1)
# dog1.sport(2)
dog1.bark()


