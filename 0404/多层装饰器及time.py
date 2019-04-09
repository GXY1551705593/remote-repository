import time
def wapper(func):
    def inner(name):
        print('登录成功',time.ctime())
        func(name)
    return inner
@wapper
def pint1(name):
    print('登陆中',name)

if __name__=='__main__':
    pint1('xiaoming')



