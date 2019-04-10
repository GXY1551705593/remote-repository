'''类的继承'''
class Dog():
    def __init__(self,gender):
        self.gender=gender
        self.__age=2
        self._name='coco'
    def bark(self):
        self.__age=33
        self._name='hh'
        print(self._name)
        print(self.__age)
        print('这只%s狗正在叫'%self.gender)
class MyDog(Dog):
    pass
dog1=MyDog('公狗')
dog1.bark()
print(dog1.__age)
