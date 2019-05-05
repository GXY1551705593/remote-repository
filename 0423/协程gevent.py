'''协程gevent'''
import gevent
import time
from gevent import monkey
#monkey.patch_all()#猴子补丁必须要加上去
def talk():
    for i in range(3):
        print('talk',i)
        #work2()
def speak():
    for i in range(3):
        print('speak',i)

p1=gevent.spawn(talk)
p1.join()
p2=gevent.spawn(speak)

p2.join()
exit()


