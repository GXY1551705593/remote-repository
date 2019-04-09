class Car(object):
    def __init__(self,mark,model,year):
        '''初始化描述汽车的属性'''
        self.mark=mark
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive(self):
        '''返回整洁的描述性信息'''
        print(self.mark,self.model,self.year,self.odometer_reading)
        '''打印一条汽车里程的消息'''
    def read_odometer(self):
        print('This car has'+' '+str(self.odometer_reading)+' '+'miles on it')
car1=Car('BMW','x4','3')
car1.odometer_reading=24
car1.get_descriptive()
car1.read_odometer()