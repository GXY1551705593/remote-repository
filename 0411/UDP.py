'''这是UDP的客服端'''
import socket

if __name__=='__main__':
    #创建UDP的客户端，创建套接字
    while True:
        udp_scoket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        udp_scoket.sendto('HELLO WORLD 桂新洋'.encode('gbk'),('192.168.44.1',8080))
        udp_scoket.close()