# def old():
#     print('jdjdjkdfksf')
# old()
# new=old
# print(old)
# print(id(old))
# print(id(new))
# print('###########################')
# def wrapper(func):
#     def inner():
#         print('购物')
#         func()
#
#     return inner
# @wrapper
# def jojncar():
#     print('加入购物车')
# @wrapper
# def cost():
#     print('付款')
# if __name__=='__main__':
#     cost()
#     jojncar()
'''创建一工厂函数'''
import time
def create(choose):
    '''
    :param choose: #选择元素
    :return: #返回装饰器对象
    '''
    def warpper(func):
        def inner():
            if choose=='第一种':
                print('1登陆验证',time.ctime(1))
            elif choose=='第二种':
                print('2登陆验证',time.asctime())
            else:
                print('登陆失败')
            func()
        return inner
    return warpper

@create('第二种')
def cost():
    print('总付款金额')
if __name__=='__main__':
    cost()
@create('第一种')
def cost1():
    print('总付款金额')
if __name__=='__main__':
    cost1()



