'''9-5尝试登录次数：在为完成练习 9-3而编写的User 类中， 添加一个名为login_attempts 的属性。编写一个名为increment_login_attempts( ) 的方法，
它将属性login_attempts 的值加1。 再编写一个名为reset_login_attempts( ) 的方法，它将属性login_attempts 的值重置为0。根据User 类创建一个实例，
再调用方法increment_login_attempts( ) 多次。 打印属性login_attempts 的值， 确认它被正确地递增； 然后， 调用方法reset_login_attempts( ) ，
并再次打印属性login_attempts 的值， 确认它被重置为0。'''
class User(object):
    '''给init方法添加first_name,last_name,gender'''
    def __init__(self,first_name,last_name,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.login_attempts=2
    '''编写一个名为increment_login_attempts( ) 的方法，
它将属性login_attempts 的值加1'''
    def increment_login_attempts(self):
        self.login_attempts+=1
        print('您已经试了%s次'%self.login_attempts)
    '''编写一个名为reset_login_attempts( ) 的方法，它将属性login_attempts 的值重置为0'''
    def reset_login_attempts(self):
        self.login_attempts=0
        print('你的次数被归%s'%self.login_attempts)
    '''打印客人信息摘要'''
    def describe_user(self):
        abstract='姓:'+self.first_name+' '+'名:'+self.last_name+' '+'性别:'+self.gender
        print(abstract)
    '''判断客人性别后，发出独特的问候'''
    def greet_user(self):
        if self.gender=='男':
            print('%s%s先生，您好！'%(self.first_name,self.last_name))
        else:
            print('%s%s小姐，您好！'%(self.first_name,self.last_name))
user1=User('张','三','男')
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()