'''
1、创建socket套接字
2、需要使用bind；来绑定端口
3、listen监听模式，等待接收用户的链接，使得套接字变成被动状态
4、accept处理用户链接
'''
import socket
#1、套接字
tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2、需要使用bind来绑定端口''.

tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
tcp_server.bind(('',9000))
#3、listen监听模式，等待接收用户的链接，使得套接字变成被动状态
tcp_server.listen()
#4、accept处理用户，返回值是一个元组
#第一个套接字是用来创建一个新的套结字用来已经完成三次握手的服务端
#第二个客服端是ip和端口
server_client_socket,addressinfo_socket=tcp_server.accept()
print(server_client_socket)
print(addressinfo_socket)
print('*****创建套结字完毕*******')
data=server_client_socket.recv(1024)
print(data.decode('gbk'))
server_client_socket.close()
tcp_server.close()
