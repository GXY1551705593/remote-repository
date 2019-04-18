'''二.	（1）.创建2个子线程，线程1、2同时对全局变量num各加100万次操作（num初始值为0），每次加1，最后执行完成打印结果，
（2）.用互斥锁解决上面题目出现的num不是200万的问题'''
import threading
num=0
def work1(*args):
    global num
    num+=1
    print(num)
def work2(*args):
    global num
    num+=1
    print(num)
if __name__=='__main__':
    ret1=threading.Thread(target=work1,args=(1000000,))
    ret2=threading.Thread(target=work2,args=(1000000,))
    ret1.start()
    ret2.start()