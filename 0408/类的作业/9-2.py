'''9-2:三家餐馆:根据你为完成练习 9-1而编写的类创建三个实例， 并对每个实例调用方法describe_restaurant() '''
class Restaurant(object):
    '''添加restaurant_name()和cuisine_type()两个属性'''
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    '''调用init中restaurant_name()和cuisine_type()的属性'''
    def __str__(self):
        return self.restaurant_name,self.cuisine_type
    '''建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法,其中前者打印前述两项信息,
    而后者打印一条消息，指出餐馆正在营业。'''
    def describe_restaurant(self):
        return self.restaurant_name,self.cuisine_type
    def open_restaurant(self):
        infornmatization=self.restaurant_name+' '+'营业时间为10：00.am—11:00.pm'
        print(infornmatization)
obj1=Restaurant('寿司店','日式料理')
obj2=Restaurant('西餐厅','西式')
obj3=Restaurant('中国餐厅','中式菜')
ret1=obj1.describe_restaurant()
ret2=obj2.describe_restaurant()
ret3=obj3.describe_restaurant()
print(ret1)
print(ret2)
print(ret3)
