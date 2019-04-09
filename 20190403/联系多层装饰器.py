'''多层装饰器'''
# def wapper1(func):
#     print('aaaaaa')
#     def inner1():
#         print('bbbbb')
#     print('cccccccccc')
#     return inner1
def wapper2(func):
    print('AAAAAAAA')
    def inner2(obj):
        print('BBBBBBBB')
        func(obj)
    print('CCCCCCCCCCCC')
    return inner2

#
# @wapper1
@wapper2
def word(obj):
    print('heoll world:',obj)
    print('heoll world:%s'%obj)


if __name__ =='__main__':
    word('李磊')

