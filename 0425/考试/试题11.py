'''	（1）.创建2个子线程，线程1、2同时对全局变量num各加100万次操作（num初始值为0），每次加1，最后执行完成打印结果，
（2）.用互斥锁解决上面题目出现的num不是200万的问题'''
import threading
import time

num = 0

def thread1(number):
    global num
    for i in range(number):
        ret=lock.acquire(True)
        print(ret)
        num +=1
        lock.release()
    print('thread1:',num)

def thread2(number):
    global num
    for i in range(number):
        ret=lock.acquire(True)
        if ret:
            num += 1
            lock.release()
    print('thread2:',num)

if __name__ == '__main__':
    lock=threading.Lock()
    first_thread=threading.Thread(target=thread1,args=(1000000,))
    second_thread=threading.Thread(target=thread2,args=(1000000,))

    first_thread.start()
    first_thread.join()
    second_thread.start()