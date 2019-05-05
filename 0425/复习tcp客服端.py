import socket
#创建套接字
tcp_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
tcp_client.connect(('',8080))
#发送消息
tcp_client.send('hello'.encode('gbk'))
#接收消息
data=tcp_client.recv(1024)
print(data.decode('gbk'))

#关闭连接
tcp_client.close()