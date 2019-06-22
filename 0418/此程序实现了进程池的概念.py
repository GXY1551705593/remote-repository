'''此程序是实现了进程池的概念'''
from multiprocessing import Manager,Pool
import os
def read(q):
    print('此时read这个函数，启动的进程是:' ,os.getpid())
    for i in range(q.qsize()):
        print('此时获取的数据',q.get())
def write(q):
    print('此时write这个函数，启动的进程是',os.getpid())
    for i in range(10):
        q.put(i)
if __name__=='__main__':
    print(os.cpu_count())
    print('主进程',os.getpid())
    que=Manager().Queue()
    po=Pool()
    po.apply(write,(que,))
    po.apply(read,(que,))
    po.close()
    po.join()