import socket
while True:
    set_conent=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    set_conent.sendto('我是大帅哥！！'.encode('gbk'),('192.168.44.1',8080))
    set_conent.close()