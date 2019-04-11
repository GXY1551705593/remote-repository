'''这是udp的客户端'''

import socket


if __name__ == '__main__':
    # 1创建UDP的客户端,创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 第一个参数表示的是地址类型，用于Internet之间的进程通信
    #第二个参数表示的是传输协议udp
    # def __init__(self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None):
    # 2、使用套接字进行收发数据 utf-8
    udp_socket.sendto('hello python'.encode('gbk'),('192.168.44.1',8080))
    # sendto(data[, flags], address) -> count
    #套接字关闭
    udp_socket.close()
    # pass1q