'''地铁交通价格调整为：6公里(含)内3元;6公里至12公里(含)4元;12公里至22公里(含)5元;22公里至32公里(含)6元;32公里以上部分，每增加1元可乘坐20公里。
使用市政交通一卡通刷卡乘坐轨道交通，每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;满150元以后的乘次，价格给予5折优惠;支出累计达到400元以后的乘次，不再享受打折优惠。
要求：假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁；每月月初小明第一次刷公交卡时，扣款5元；编写程序，
从键盘获取距离，帮小明计算，如果不使用市政交通一卡通的每月总费用，和使用市政交通一卡通的每月总费用'''
class Expense(object):
    def __init__(self,distance):
        #self.cost=cost
        self.count=20
        self.distance=distance
    def with_card_cost(self):
        if self.distance<=6:
            mouth_cost=3*40
            #print(mouth_cost)
        elif 6<self.distance<=12:
            mouth_cost = 4 * 40
            #print(mouth_cost)
        elif 12 < self.distance <= 22:
            mouth_cost = 5 * 40
            #print(mouth_cost)
        elif 22< self.distance <=32:
            mouth_cost = 6* 40
           # print(mouth_cost)
        elif self.distance>32:
            mouth_cost =int(7+(self.distance-32)/32)*40
            #print(mouth_cost)
        return mouth_cost

    def without_card_cost(self):
        if self.distance <= 6:
            for i in range(40):
                if cost1>=100:
                    cost1=5
                    cost1+=3
                    print(cost1)

                #mouth_cost=5
                # while mouth_cost=3:
                #     print(mouth_cost)
                # if mouth_cost>=100:
                #     print(i)
            # mouth_cost = ((3*33+5)-100)*0.8+100
            # # print(mouth_cost)
        # elif 6 < self.distance <= 12:
        #     mouth_cost = ((4*39+5)-150)*0.5+50*0.8+100
        #     # print(mouth_cost)
        # elif 12 < self.distance <= 22:
        #     mouth_cost = (5+39*5)
        #     # print(mouth_cost)
        # elif 22 < self.distance <= 32:
        #     mouth_cost = 100+0.8*14
        # # print(mouth_cost)
        # elif self.distance > 32:
        #     mouth_cost = int(7 + (self.distance - 32) / 20) * 20
        #     # print(mouth_cost)
        #return cost
ret=Expense(5)
print(ret.with_card_cost())
print(ret.without_card_cost())




