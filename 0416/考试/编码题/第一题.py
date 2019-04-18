#使用Process创建1个子进程，让子进程每1秒钟打印1个数字，数字从1开始一直到10，即1.2.3......10
import time

for i in range(1,11):
    time.sleep(1)
    print(i)

