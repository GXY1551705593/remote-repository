def deco1(func):
    print(1)
    def wrapper1():
        print(2)
        func()
        print(3)
    print(4)
    return wrapper1

def deco2(func):
    print(5)
    def wrapper2():
        print(6)
        func()
        print(7)
    print(8)
    return wrapper2
def deco3(func):
    print(9)
    def wrapper3():
        print(10)
        func()
        print(11)
    print(12)
    return wrapper3

@deco1
@deco2
@deco3
def cost():
    print('cost')


if __name__ == '__main__':
    cost()
