# 编码题
# 一. 使用Process创建1个子进程，让子进程每1秒钟打印1个数字，数字从1开始一直到10，即1.2.3......10
import threading
import time
def my_num():
    for i in range(11):
        if i==0:
            i==0
        else:
            time.sleep(1)
            print(i)
if __name__ == '__main__':
    my_num_thread = threading.Thread(target=my_num)
    my_num_thread.start()