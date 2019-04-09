'''2、现有一项业务 ：“BMW 4SJoker在店买了一俩BMW X7”，根据业务描述，声明相关类。'''
class Person(object):
    def __init__(self,name):
        self.name=name
class Carshop(object):
    def __init__(self,shop):
        self.shop=shop
    def run(self):
        print('这家店正在运营')
class Mark(object):
    def __init__(self,mark):
        self.mark=mark

person=Person('Joker')
carshop=Carshop('BMW 4S')
mark1=Mark('BMW X7')
print(person.name)
print(carshop.shop)
print(mark1.mark)

