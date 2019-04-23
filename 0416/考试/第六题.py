'''求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。'''
while True:
    a=int(input('输入a：'))

    if len(str(a))==1:
        count = int(input('输入相加次数：'))
        def add(a,count):
            '''

            :param a: #a为数字
            :param count: #输入相加次数
            :return:
            '''
            list_new = []#建立空列表
            s = 0#给s赋值0
            a=str(a)#将a转化为字符串
            for i in range(1,count+1):
                list_new.append(int(a*i))
                print(list_new[i-1],end=" ")
                if i<count:
                    print("+",end=" ")
            for j in list_new:
                s += j
            print( '=',s)
            #return s

        add(a,count)
    else:
        print('a输入错误')
