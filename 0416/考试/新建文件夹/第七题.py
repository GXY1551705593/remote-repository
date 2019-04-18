#嵌套循环输出10-50中个位带有1-5的所有数字
for i in range(10,51):
    if 1<=i%10<=5:
        print(i)