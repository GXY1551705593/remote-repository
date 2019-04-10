class Dog():
    def __init__(self,gender):
        self.gender=gender
    def bark(self):
        print('这只%s狗正在叫'%self.gender)