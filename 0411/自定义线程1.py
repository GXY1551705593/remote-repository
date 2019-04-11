import threading
class My_Thread(threading.Thread):
    def __init__(self,age):
        super(My_Thread, self).__init__()
        self.age
    def informzaitoin(self):
        print('他正在说话')
if __name__=='__main__':
    My_Thread()