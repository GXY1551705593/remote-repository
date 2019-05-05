# 二.	（1）.创建2个子线程，线程1、2同时对全局变量num各加100万次操作（num初始值为0），每次加1，最后执行完成打印结果，
import threading
num = 0
def socket1():
    global num
    for i in range(1000000):
        num = num+1
        i +=1
    print(num)
def socket2():
    global num
    for i in range(1000000):
        num = num+1
        i +=1
    print(num)

if __name__ == '__main__':
    socket1_num = threading.Thread(target=socket1)
    socket1_num.start()
    socket2_num = threading.Thread(target=socket1)
    socket2_num.start()
