'''3、创建一个由有序数值对(x, y) 组成的 Point 类，它代表某个点的 X 坐标和 Y 坐标。
X 坐标和 Y 坐标在实例化时被传递给构造器，
如果没有给出它们的值，则默认为坐标的原点。'''
class Point(object):
    '''添加属性'''
    def __init__(self):
        pass
    def position(self,x=0,y=0):#添加positon方法，默认为坐标的原点
        #print(x,y)
        return x,y
point=Point()
print(point.position())
