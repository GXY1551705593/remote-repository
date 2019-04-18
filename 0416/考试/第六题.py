'''求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。'''
a=int(input('输入数字：'))
n=int(input('输入尾数位数：'))
list=[]

for i in range(a,a*(10**2)):
    print(i)