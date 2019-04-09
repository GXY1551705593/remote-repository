'''9-3 用户:创建一个名为User 的类， 其中包含属性first_name 和last_name，还有用户简介通常会存储的其他几个属性。在类User中
定义一个名为describe_user( ) 的方法， 它打印用户信息摘要； 再定义一个名为greet_user( ) 的方法， 它向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。'''
class User(object):
    '''添加first_name,last_name,gender属性'''
    def __init__(self,first_name,last_name,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
    '''定义一个名为describe_user( ) 的方法， 它打印用户信息摘要'''
    def describe_user(self):
        abstract='姓:'+self.first_name+' '+'名:'+self.last_name+' '+'性别:'+self.gender
        print(abstract)
    '''定义一个名为greet_user( ) 的方法， 它向用户发出个性化的问候'''
    def greet_user(self):
        if self.gender=='男':
            print('%s%s先生，您好！'%(self.first_name,self.last_name))
        else:
            print('%s%s小姐，您好！'%(self.first_name,self.last_name))
user1=User('张','三','男')
user1.describe_user()
user1.greet_user()
user2=User('李','四','女')
user2.describe_user()
user2.greet_user()