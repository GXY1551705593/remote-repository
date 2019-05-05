'''求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。'''
while True:
    num=int(input('输入最后一位数：'))
    list=[]
    for i in range(1,num+1):
        list.append(int(str(num)[0]*i))
        if len(str(list[-1]))==len(str(num)):
            total=sum(list)
            print('表格%s的和为%s:'%(list,total))

