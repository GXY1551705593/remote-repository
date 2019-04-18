#创建两个udp程序·，如udpA能接收，udpB发送的数据并·打印出来· 
import socket
import threading
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('',4000))
def send():
    while True:
        conent=input('请输入内容:')
        udp_socket.sendto(conent.encode('gbk'),('192.168.44.1',8080))
def receive():
    while True:
        data,address=udp_socket.recvfrom(1024)
        data = data.decode('gbk')
        print('发送内容：',data)
if __name__=='__main__':
    ret=threading.Thread(target=send)
    ret2 = threading.Thread(target=receive)
    ret.start()
    ret2.start()

