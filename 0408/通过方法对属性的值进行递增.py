class Car(object):
    def __init__(self,mark,model,year):
        '''初始化描述汽车的属性'''
        self.mark=mark
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive(self):
        '''返回整洁的描述性信息'''
        print(self.mark, self.model, self.year, self.odometer_reading)
        '''打印一条汽车里程的消息'''
    def update_odometer(self, mileage):
        '''将里程表值设定为指定的值'''
        self.odometer_reading = mileage
    def increment_odometer(self,miles):
        '''将里程表读数增加指定的量'''
        self.odometer_reading += miles
    def read_odometer(self):
        '''描述这辆车的油量状态'''
        print('This car has'+' '+str(self.odometer_reading)+' '+'miles on it')
car1=Car('BWD','x4','3')
car1.get_descriptive()
car1.update_odometer(2200)
car1.read_odometer()
car1.increment_odometer(100)
car1.read_odometer()
