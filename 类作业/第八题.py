'''8、使用while，再完成以下图形的输出.'''
class Rhombus(object):
    def __init__(self):
        pass
    def print(self):#给出方法，完成图形的输出
        i = 0
        while i < 9: # 总循环次数 9
            if i < 5:
                # 上空格部分
                j = 0
                while j < 4 - i:
                    print(" ",end="")
                    j +=1
                #上部分
                j = 0
                while j < i+1:
                    print("*", end=" ")
                    j +=1
            else:
                # 下空格部分
                j = 0
                while j < i -4:
                    print(" ",end="")
                    j +=1
                # 下部分
                j = 0
                while j < 9 - i:
                    print("*",end=" ")
                    j +=1
            print()
            i += 1
rhombus=Rhombus()
print(rhombus.print())



