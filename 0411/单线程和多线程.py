import threading
import time
def eat():
    for i in range(3):

        print('A在吃饭',i)
        #time.sleep(1)
def talk():
    for i in range(3):
        print('B在说话')
if __name__=='__main__':
    #print(threading.enumerate())
    ret=threading.Thread(target=eat)
    ret1=threading.Thread(target=talk)

    #print(threading.enumerate())
    #ret.setDaemon(True)
    ret.start()

    #ret1.setDaemon(True)
    ret1.start()
    #print('程序结束')
    #exit()

