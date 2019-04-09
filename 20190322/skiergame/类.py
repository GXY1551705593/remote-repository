'''
class dog:
    def _new_(self,):
        def __init__(self,name,age):
            self.name=name
            self.age=age
        #def run(self):
            #print('这只狗正在跑')
    def bark(self):
        print('这只狗正在叫')
    def eat(self):
        print('这只狗正在吃饭')
dog1=dog('小白',10)
print(dog1.name,dog1.age)
#1、要求：记录力的品牌mark,颜色color、价格price、速度speed等特征，并实现增加车辆信息、显示全部车辆信息的功能。
class Car:

    def __init__(self,mark,color,price,speed):
        self.mark=mark
        self.color=color
        self.price=price
        self.speed=speed

    def infor(self):
        print(self.mark,self.color,self.price,self.speed)

car1=Car('捷安特','bule','$100','60')
car1.infor()'''
class Chinese:
    '这是一个中国人的类'
    government='中国人民政府'
    def face():
        print('黄色')
print(Chinese.government)
Chinese.face()
#实例化到底干了什么？
# p1=Chinese()
# print(p1)

