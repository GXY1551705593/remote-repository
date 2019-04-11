'''实现多线程，借助包'''
import threading


def coding():
    #for i in range(5):
        print('敲代码')



def smoking():
    for i in range(5):
        print('正在抽烟',i)



if __name__ == '__main__':
    print('刚刚进入程序',threading.enumerate())
    # 这个函数显示的是活动的线程个数


    coding_thread = threading.Thread(target=coding)
    # threading:写多线程的模块,target这个参数指定的是线程需要执行的函数
    smoking_thread = threading.Thread(target=smoking)
    # print(coding_thread)
    # print(smoking_thread)
    print('创建线程之后',threading.enumerate())

    # 开启线程
    coding_thread.start()
    smoking_thread.start()

    print('线程启动之后', threading.enumerate())
