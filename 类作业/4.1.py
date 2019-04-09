'''1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息'''
class Person(object):
    '''添加属性，属性有姓名、年龄、性别，'''
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personinfo(self):#创建方法personInfo,打印这个人的信息
        return self.name,self.age,self.gender
person=Person('小明',18,'男')
print(person.personinfo())
print('###################################################')












