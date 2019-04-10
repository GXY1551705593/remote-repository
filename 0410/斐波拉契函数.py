'''创建斐波拉契函数'''

def fobi(num):
    a=0
    b=1
    index=0
    print(111111111)
    while index<num:

        a,b=b,a+b
        index+=1
        print(2222222222)
        yield b
        print(33333333333)
if __name__=='__main__':
    ret=fobi(5)
    for i in ret:
        print(i)