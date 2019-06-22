'''1、将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
- 输入描述:将一个英文语句以单词为单位逆序排放。
- 输出描述:得到逆序的句子
示例1
- 输入
I am a boy
- 输出
boy a am I'''
str=input('请输入：')
list_str=str.split()[ : :-1]#将字符串转化为列表并倒叙
str_new=""  #创建新字符串
for i in list_str:#遍历列表
    str_new+=i+' '
    # print(len(str_new))
    '''- 输出描述:得到逆序的句子，- 输出，boy a am I'''
    if len(str_new)==len(str)+1:
        print(str_new)
        break

# while True:
#     list_str=input('请输入：').split()#将字符串转化为列表并倒叙
#     list_str.reverse()
#     print(' '.join(list_str))
