'''9-4 就餐人数 ： 在为完成练习 9-1而编写的程序中， 添加一个名为number_served 的属性， 并将其默认值设置为0。 根据这个类创建一
个名为restaurant 的实例； 打印有多少人在这家餐馆就餐过， 然后修改这个值并再次打印它。添加一个名为set_number_served( ) 的方法，
它让你能够设置就餐人数。调用这个方法并向它传递一个值， 然后再次打印这个值。添加一个名为increment_number_served( ) 的方法，
它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值： 你认为这家餐馆每天可能接待的就餐人数。'''
class Restaurant(object):
    '''添加restaurant_name 和cuisine_type两个属性'''
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served =0
    '''调用init中restaurant_name 和cuisine_type的属性'''
    def __str__(self):
        return self.restaurant_name,self.cuisine_type,self.number_served
    '''建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法,其中前者打印前述两项信息,
    而后者打印一条消息，指出餐馆正在营业。'''
    def describe_restaurant(self):
        return self.restaurant_name,self.cuisine_type
    def open_restaurant(self):
        infornmatization=self.restaurant_name+' '+'营业时间为10：00.am—11:00.pm'
        print(infornmatization)
    def set_number_served(self,served):
        self.number_served=served
        print('这个餐厅接待人数：%s'% self.number_served)
    def increment_number_served(self,add_served):
        self.number_served+=add_served
        print('这家餐厅增加到%s人'% self.number_served)
restaurant=Restaurant('寿司店','日式料理')
restaurant.number_served=25
ret=restaurant.__str__()
restaurant.open_restaurant()
restaurant.set_number_served(20)
restaurant.increment_number_served(30)
print(ret)
