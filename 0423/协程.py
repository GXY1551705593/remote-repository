import time
def talk():
    for i in range(5):
        print('说话',i)
        time.sleep(1)
def sing():
    for i in range(5):
        print('唱歌',i)
        time.sleep(1)
p1=talk()
p2=sing()
if __name__ == '__main__':
    
    print(next(p1))
    print(next(p2))