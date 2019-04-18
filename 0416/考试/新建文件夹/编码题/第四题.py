'''四.创建一个tcp服务器
（1）能接收tcp客户端发来的请求
（2）能并发处理客户端连接
（3）能接收tcp客户端发来的数据、每次收到数据打印出来并dA回复客户端“已收到！谢谢！”、直到客户端主动断开（线程版）'''
import socket
tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、需要使用bind来绑定端口
tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
tcp_socket.bind(" ",5000)
tcp_socket.send('123'.encode('gbk'),('192.168.44.1',8080))
tcp_socket.listen()