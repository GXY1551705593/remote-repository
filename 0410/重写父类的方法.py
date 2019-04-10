'''类的继承'''
class Dog():
    def __init__(self,gender):
        self.gender=gender
    def bark(self):
        print('这只%s狗正在叫'%self.gender)
class MyDog(Dog):
    def __init__(self,gender):
        super().__init__(gender)
    def bark(self):
        print('这只%s狗正在大声叫'%self.gender)
dog1=Dog('公')
ret=dog1.gender
print(ret)
dog2=MyDog('母狗')
dog2.bark()
