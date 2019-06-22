'''给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。
S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
输入: J = "aA", S = "aAAbbbb"
输出: 3'''
J =input('输入J:')
S = input('输入S:')
def matching(J,S):
    '''

    :param J: #给定字符串J 代表石头中宝石的类型
    :param S:#字符串 S代表你拥有的石头
    :return:
    '''
    m=len(J)
    len(J)<=50,len(S)<=50
    i,nums=0,0
    while i<m :
        nums+=S.count(J[i])
        i += 1
    return nums
if __name__ == '__main__':
    ret=matching(J,S)
    print(ret)

