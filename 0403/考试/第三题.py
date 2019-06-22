'''有一个己经排好序的数组1 = [0,10,20,30,40,50]。现输入 一个数，要求按原来的规律将它插入数组中'''
class List(object):
    def __init__(self,new_number):#添加数组属性输入数字
        self.new_number=new_number
    def change(self):#用change方法，按原来的规律将它插入数组中
        list_old = [0, 10, 20, 30, 40, 50,self.new_number]
        list_new = []
        #new_number=input('')
        for i in list_old:
            list_new.append(i)
            if len(list_new) == 6:
            #此处目的在于用原来规律它插入数组中
                if self.new_number>=50:
                    list_new.append(self.new_number)
                elif self.new_number>=40:
                    list_new.insert(5,self.new_number)
                elif self.new_number >= 30:
                    list_new.insert(4, self.new_number)
                elif self.new_number >= 20:
                    list_new.insert(3, self.new_number)
                elif self.new_number >= 10:
                    list_new.insert(2, self.new_number)
                elif self.new_number >= 0:
                    list_new.insert(1, self.new_number)
                else:
                    list_new.insert(0,self.new_number)
                return list_new

list1=List(401)
print(list1.change())


