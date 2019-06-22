'''2给定两个由小写字母构成的字符串A和B ，只要我们可以通过交换
A中的两个字母得到与B相等的结果，就返回true ；否则返回false 。
示例1：
输入： A = "ab", B = "ba"
输出： true

示例2：
输入： A = "ab", B = "ab"
输出： false

示例3:
输入： A = "aa", B = "aa"
输出： true

示例4：
输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true

示例5：
输入： A = "", B = "aa"
输出： false'''
# while True:
while True:
    A =input('输入字符串A：')
    B =input('输入字符串B：')
    if sorted(A)==sorted(B):
        print('true')
    else:
        print('false')