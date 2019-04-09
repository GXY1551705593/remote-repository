class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age,gender):
        '''初始化小狗名字、年龄和性别'''
        self.name=name
        self.age=age
        self.gender=gender
    def sit_down(self):#命令小狗蹲下
        status=self.age+'岁的，性别为'+self.gender+' '+self.name+' '+'is now sitting'
        return status
        #print(self.name)
dog1=Dog('xiaohua','2','female')
ret=dog1.sit_down()
print(ret)