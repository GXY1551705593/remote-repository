'''1、要求：记录车的品牌mark,颜色color、价格price、速度speed等特征，
并实现增加车辆信息、显示全部车辆信息的功能。'''
class Car(object):
    def __init__(self,mark,color,price,speed):
        self.mark=mark
        self.color=color
        self.price=price
        self.speed=speed
    def information(self):
        print('这辆速度为%s的%s%s车价格是%s'%(self.speed,self.color,self.mark,self.price))
car1=Car('奔驰','黑色','50万','120kw/h')
car1.information()