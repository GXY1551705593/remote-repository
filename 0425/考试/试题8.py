'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？'''

I = float(input("请输入当月利润，单位为万元："))
if I <= 10:
    num  = 10 * 0.1
elif 10 < I <= 20:
    num = 10 * 0.1 + (I-10) * 0.075
elif 20 < I <= 40:
    num = 10 * 0.1 + 10 * 0.075 + (I-20) * 0.05
elif 40 < I <= 60:
    num = 10 * 0.1+ 10 * 0.075 + 20 * 0.05 + (I-40) * 0.03
elif 60 < I <= 100:
    num = 10 * 0.1+ 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (I-60) * 0.015
elif I > 100:
    num = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (I-100) * 0.015
print(num,'万元')
print(I)