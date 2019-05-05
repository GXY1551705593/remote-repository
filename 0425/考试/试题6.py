'''求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。'''
a=input("输入数字:")
count=int(input("几个数字相加:"))
list1=[]
for i in range(1,count+1):
    list1.append(int(a*i))
    print(list1[i-1])
print(sum(list1))