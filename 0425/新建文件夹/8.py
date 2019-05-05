
# （2）.用互斥锁解决上面题目出现的num不是200万的问题
import threading

lock =threading.Lock

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
import time

if __name__ == '__main__':

    socket1_num = threading.Thread(target=socket1)
    socket1_num.start()
    time.sleep(0.5)
    socket2_num = threading.Thread(target=socket1)
    socket2_num.start()
