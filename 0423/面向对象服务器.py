"""该程序主要为了面向对象而设计"""
import socket
class Serve():
    def __init__(self):
          pass
    def main(self):
        '''主函数，实现逻辑'''
        #创建套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #固定端口
        server_socket.bind(('', 8080))
        server_socket.listen()




