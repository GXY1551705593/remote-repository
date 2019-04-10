'''将实例作为属性表示'''
class Dog():
    def __init__(self,age):
        self.age=age
    def bark(self):
        print('这只%s的狗正在叫'%self.age)
class Dog_gender():
    def __init__(self,gender='公狗'):
        self.gender=gender
    def eat(self):
        return ('这只%s狗正在吃东西'%self.gender)
class MyDog(Dog):
    def __init__(self,name):
        super().__init__(name)
        self.gender=Dog_gender()

dog1=MyDog('')
print(dog1.gender.eat())

