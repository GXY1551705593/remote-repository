'''这个程序实现了进程池的概念'''
from multiprocessing import Manager,Pool
import os
def read(q):
    print(os.getpgid())
    for i in range(q.qsize()):
        print(q.get())
def write(q):
    print(os.getpgid())
    for i in range(10):
        q.put(i)
if __name__=='__main__':
    que=Manager().Queue()
    po=Pool()
    po.apply(write,(que,))
    po.apply(read,(que,))
    po.close()
    po.join()