'''5、要求：创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。在类User中
定义一个名为describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。'''
class User(object):
    '''属性first_name和last_name'''
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):#describe_user方法，它打印用户信息摘要
        return self.first_name,self.last_name
    def greet_user(self):#一个名为greet_user()方法，它向用户发出个性化
        return '你好'
use1=User('王','小明')
print(use1.describe_user(),use1.greet_user())