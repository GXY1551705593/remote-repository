# import socket
# tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
# tcp_socket.bind(('',8080))
# tcp_socket.listen()
# data,adress=tcp_socket.accept()
# print(data)
# print(adress)
# revice_conent=data.recv(1024)
# print(revice_conent.decode('gbk'))
# data.close()
# tcp_socket.close()

# import socket
# tcp_sever=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcp_sever.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
# tcp_sever.bind(('',8080))
#
# tcp_sever.listen()
#
# data,adress=tcp_sever.accept()
# print(data)
# print(adress)
# print('创建套接字完毕')
# conent=data.recv(1024)
# print(conent.decode('gbk'))
# data.close()
# tcp_sever.close()
#

# import socket
# #创建套接字
# tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定端口
# tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
# tcp_socket.bind(('',8080))
# #监听端口
# tcp_socket.listen()
#
# data,adress=tcp_socket.accept()
#
# print(data)
# print(adress)
# #创建套接字完毕
# conent=data.recv(1024)
# print(conent.decode('gbk'))
# data.close()
# tcp_socket.close()






































