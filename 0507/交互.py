'''这个程序执行的模拟商城购物情况'''
import pymysql


class ShangHui(object):
    def __init__(self):
        # 只需要连接一次
        self.connect = pymysql.connect(host='localhost', port=3306,
                                       database='shuju', user='root', password='mysql', charset='utf8')
        self.cur = self.connect.cursor()

    def login(self):
        inname = input('请输入用户名')
        inpassword = input('请输入密码')
        # 拼接sql字符串
        sql = 'select * from user where name=%s and password=%s'
        # sql = 'select * from user where name=inname and password=inpassword'
        # print(sql)

        ret = self.cur.execute(sql, [inname, inpassword])
        print(ret)
        if ret == 0:
            print('用户名或者密码错误')
            return
        print('########登录成功#############')

    def register(self):
        # 1、判断用户是否在当前的用户表里(保证用户名的唯一性)
        inname = input('请输入用户名')
        inpassword = input('请输入密码')
        sql = 'select * from user where name=%s'
        ret = self.cur.execute(sql, [inname])
        if ret:
            print('用户名已经存在')
            return

        # 2、如果没有则插入数据库
        sql_insert = 'insert into user VALUES(0,%s,%s)'
        self.cur.execute(sql_insert, [inname, inpassword])
        # 3 注意修改数据库的数据需要提交
        self.connect.commit()
        print('注册成功')

    def change(self):
        # 判断用户名、密码输入是否正确
        inname = input('请输入用户名')
        inpassword = input('请输入密码')
        sql = 'select * from user where name=%s'
        ret = self.cur.execute(sql, [inname])
        if ret:
            print('用户名已经存在')

            # 修改密码
            inname = input('请再次输入用户名')
            inpassword_update = input('输入修改密码')
            sql_update = 'update user set password=%s where name=%s'
            self.cur.execute(sql_update, [inpassword_update, inname])
            # 提交
            self.connect.commit()
            print('修改成功')

    def showgood(self):
        sql_showgood = 'select name,price from goods'
        self.cur.execute(sql_showgood)
        ret = self.cur.fetchall()
        print('商品展示')
        for i in ret:
            print(i)

    def order(self):
        # 商品展示
        sql_showgood = 'select name,price from goods'
        self.cur.execute(sql_showgood)
        ret = self.cur.fetchall()
        print('商品展示')
        for i in ret:
            print(i)
        # 选择商品
        inname_goods = input('输入商品')
        sql_choosegoods = 'select name from goods where name=%s'
        self.cur.execute(sql_choosegoods, [inname_goods])
        if self.cur:
            ret = self.cur.fetchall()
            for i in ret:
                print(i)
                # 下单
                sql_joinshopcar = 'insert into orders values(0,%s)'
                self.cur.execute(sql_joinshopcar, [i])
                self.connect.commit()
                sql_show = 'select * from orders'
                self.cur.execute(sql_show)
                ret = self.cur.fetchall()
                for j in ret:
                    print('下单成功', j)

        # print('下单')

    def printinfo(self):
        print('欢迎来到尚惠有品商城')
        print('1-登录')
        print('2-注册')
        print('3-修改')
        print('4-商品展示')
        print('5-下单')
        print('6-退出')

        while True:
            choose = input('请输入需要执行的操作:')
            if choose == '1':
                self.login()

            elif choose == '2':
                self.register()

            elif choose == '3':
                self.change()

            elif choose == '4':
                self.showgood()

            elif choose == '5':
                self.order()

            elif choose == '6':
                break

            else:
                print('输入错误')


if __name__ == '__main__':
    shanghui = ShangHui()
    shanghui.printinfo()
