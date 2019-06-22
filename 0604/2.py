#1、十进制数转二进制数，二进制以字符串形式输出。  例如十进制6输出 110
while True:
    num=int(input('输入十进制数字：'))
    print('输出二进制数：',bin(num))
    print('二进制以字符串形式输出',type(str(bin(num))))