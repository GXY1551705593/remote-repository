'''类的继承'''
class Dog():
    def __init__(self,gender):
        self.gender=gender
    def bark(self):
        print('这只%s狗正在叫'%self.gender)
class MyDog(Dog):
    def __init__(self,gender):
        super().__init__(gender)
        self.age='2岁'
    def jump(self):
        print('%s正在跳'%self.gender)
    def infor(self):
        print('这只%s是%s'%(self.gender,self.age))
dog1=Dog('公')
dog1.bark()
dog2=MyDog('母狗')
dog2.bark()
dog2.jump()
dog2.infor()
