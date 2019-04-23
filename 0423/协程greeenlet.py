from greenlet import greenlet
import time
def work1():
    for i in range(3):
        print('work1',i)
        p2.switch()
        time.sleep(1)
def work2():
    for i in range(3):
        print('work2',i)
        p1.switch()
        time.sleep(1)

p1=greenlet(work1)
p2=greenlet(work2)
p1.switch()
p2.switch()


