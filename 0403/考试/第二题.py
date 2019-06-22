'''假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多 少种不同的方法爬到楼顶部？'''
def steps(n):
    '''

    :param n: #输入总步数
    :return: #返回方法数量
    '''
    if 0<n<=2:
        return n
    else:
        return steps(n-2)+steps(n-1)
ret=steps(7)
print(ret)




