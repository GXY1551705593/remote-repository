'''进程池'''
from multiprocessing import Pool
import os
def work():
    print('开始执行，此时的进程编号：',os.getpgid())
po=Pool(1)
print(type(po))
for i in range(10):
    po.apply_async(work,(i,))
print('*****开始******')
po.close()
po.join()
print('******结束******')
