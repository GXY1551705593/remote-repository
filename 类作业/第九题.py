'''有如下列表，nums=[2,7,11,15,1,8,7],请找到列表中任意两个元素相加能够等于9的元素集合，列[(2,7), (1,8)]'''
class Set(object):
    def __init__(self):
        pass
    def add(self):#用add方法找到列表中任意两个元素相加能够等于9的元素集合，
        nums = [2, 7, 11, 15, 1, 8, 7]
        # for i in nums:
        #     for j in nums:
        #         if i+j==9:
        return [(i,j) for i in nums for j in nums if i+j==9 ]#用列表推导式，列出集合
set1=Set()
print(set(set1.add()))