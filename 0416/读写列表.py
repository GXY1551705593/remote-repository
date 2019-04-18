import threading
list_old=[1,2,3,4,5,6]
def read():
    for i in list_old:
        print(i)
def write():
    list_new=[]
    for j in list_old:
        list_new.append(j)
        if len(list_new)==6:
            print(list_new)
if __name__=='__main__':
    ret=threading.Thread(target=read,args=())
    ret2=threading.Thread(target=write)
    ret.start()
    ret2.start()