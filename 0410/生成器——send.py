'''创建斐波拉契函数'''

def fobi(num):
    a=0
    b=1
    index=0
    while index<num:

        a,b=b,a+b
        index+=1

        yield b
if __name__=='__main__':
    ret=fobi(5)
    print(ret.send(None))
    print(ret.send(1))
    print(ret.send(1))
    print(ret.send(1))
    print(ret.send(1))


