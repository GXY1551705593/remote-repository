'''9-1:餐馆 ： 创建一个名为Restaurant的类，其方法__init__( ) 设置两个属性： restaurant_name 和cuisine_type 。 创建一个名为
describe_restaurant( ) 的方法和一个名为open_restaurant( ) 的方法， 其中前者打印前述两项信息， 而后者打印一条消息，
指出餐馆正在营业。根据这个类创建一个名为restaurant 的实例， 分别打印其两个属性， 再调用前述两个方法。'''
class Restaurant(object):
    '''添加restaurant_name 和cuisine_type两个属性'''
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    '''调用init中restaurant_name 和cuisine_type的属性'''
    def __str__(self):
        return self.restaurant_name,self.cuisine_type
    '''建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法,其中前者打印前述两项信息,
    而后者打印一条消息，指出餐馆正在营业。'''
    def describe_restaurant(self):
        return self.restaurant_name,self.cuisine_type
    def open_restaurant(self):
        infornmatization=self.restaurant_name+' '+'营业时间为10：00.am—11:00.pm'
        print(infornmatization)
obj=Restaurant('寿司店','日式料理')
ret=obj.__str__()
ret2=obj.describe_restaurant()
obj.open_restaurant()
print(ret)
print(ret2)


