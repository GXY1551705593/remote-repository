'''实现多线程的聊天软件'''
import threading
import socket

udp_socket = None


def senddata():
    while True:
        sendinfo = input('请输入需要传输的数据')
        udp_socket.sendto(sendinfo.encode('gbk'),('172.27.35.1',8080))
def recvdata():

    while True:
        data, address_info = udp_socket.recvfrom(1024)
        print('发送人:%s,接收的信息是：%s' % (address_info, data.decode('gbk')))

def main():
    '''
    这个主函数实现的是聊天软件，多线程实现，一个线程实现接收，一个线程执行发送
    :return:
    '''
    global udp_socket
    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2、绑定地址
    udp_socket.bind(("", 9300))

    # +接收与发送(多线程的方式)
    sendthread = threading.Thread(target=senddata)
    recvthread = threading.Thread(target=recvdata)

    sendthread.start()
    recvthread.start()

    pass


if __name__ == '__main__':
    main()
