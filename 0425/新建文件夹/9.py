# 三.创建两个udp程序·，如udpA能接收，udpB发送的数据并·打印出来· 
import socket
import threading
udp_socket = None
def recv():
    global udp_socket
    while True:
        udp_recv,ip = udp_socket.recvfrom(1024)
        print("输入的是：%s,发来的ip是:%s"%udp_recv,ip)
def send():
    global udp_socket
    while True:
        udp_send=input("发送：")
        udp_socket.sendto(udp_socket.encode('utf-8'),('192.168.58.136',8080))

if __name__ == '__main__':

    #1创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2绑定ｉｐ
    udp_socket.bind(('192.168.58.136',6580))
    recv_thread = threading.Thread(target=recv)
    recv_thread.start()
    send_thread = threading.Thread(target=send)
    send_thread.start()
