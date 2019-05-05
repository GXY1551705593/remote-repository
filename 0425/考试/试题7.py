'''嵌套循环输出10-50中个位带有1-5的所有数字'''
list1=[]
for i in range(10,51):
    if i%10<=5 and i%10!=0:
        list1.append(i)
print(list1)
