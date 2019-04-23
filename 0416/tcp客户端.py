'''客户端'''

import socket
    # # 1、套接字
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2、创建链接

tcp_socket.connect(('192.168.44.1',8080))

    # 3、发送信息

tcp_socket.send('你好'.encode('gbk'))
    # 4、接收数据
ret = tcp_socket.recv(1024)
print(ret.decode('gbk'))

tcp_socket.close()