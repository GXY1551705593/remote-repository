'''7、有如下值集合[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，
将小于66的值保存至第二个key的值中.即：{'k1':大于66的所有值,'k2':小于66的所有值}'''
class Dictory(object):
    def __init__(self):
        pass
    '''将所有大于66的值保存至字典的第一个key中，
将小于66的值保存至第二个key的值中'''
    def save(self):
        dict={}
        list=[11,22,33,44,55,66,77,88,99,90]
        list_k1=[]
        list_k2=[]
        for i in list:#利用for循环
            if i>66:
                list_k2.append(i)
                #print(i)
                dict['k2']=list_k2

            elif i<66:
                list_k1.append(i)
                dict['k1']=list_k1
        return dict
dict1=Dictory()
print(dict1.save())

