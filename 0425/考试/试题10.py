'''使用Process创建1个子进程，让子进程每1秒钟打印1个数字，数字从1开始一直到10，即1.2.3......10'''
import threading
import time
def Proccess():
    for i in range(1,11):
        print(i)
        time.sleep(1)

if __name__ == '__main__':
    Proccess_thread=threading.Thread(target=Proccess)
    # Proccess_thread.join()
    Proccess_thread.start()
