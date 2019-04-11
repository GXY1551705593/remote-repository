try:
    a=int(input('输入分子:'))
    b=int(input('输入分母:'))
    n=a/b
    print(n)
    print('#########')
except Exception as e:
    print(e)
    print('************')
#from collections import Iterator


m=int(input('输入数字：'))
while True:
    try:
        ret=(i for i in range(m))
        print(next(ret))
        print(next(ret))

    except StopIteration as e:
        print('超出范围')
# ret=(i for i in range(2))
# print(next(ret))