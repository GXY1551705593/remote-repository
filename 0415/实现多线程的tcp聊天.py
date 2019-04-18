'''实现多线程的tcp聊天'''
import threading
def talk():
    print('你好')
    print('你好')
    print('你好')
if __name__=='__main__':
    ret=threading.Thread(target=talk())
    ret.setDaemon(True)
    ret.start()