'''2、创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，
调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，创建方法study参数为Teacher对象，
调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’
xxx为老师的teach方法返回的信息。重写__str__方法，返回student的信息。'''
class Person(object):
    pass
    # '''添加属性，属性有姓名、年龄、性别，'''
    # def __init__(self,name,age,gender):
    #     self.name=name
    #     self.age=age
    #     self.gender=gender
    # def personinfo(self):#创建方法personInfo,打印这个人的信息
    #     return self.name,self.age,self.gender
class Student(Person):
    def __init__(self,name,age,gender,college,class_):
        self.name = name
        self.age=age
        self.gender=gender
        self.college=college
        self.class_=class_
    def personinfo(self):
        return self.name,self.age,self.gender,self.college,self.class_
