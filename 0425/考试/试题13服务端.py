'''四.创建一个tcp服务器
（1）能接收tcp客户端发来的请求
（2）能并发处理客户端连接
（3）能接收tcp客户端发来的数据、每次收到数据打印出来并dA回复客户端“已收到！谢谢！”、直到客户端主动断开（线程版）
'''
import threading
import socket

def tcp_client():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(('',8080))
    tcp_socket.send('',8080)
    ret=tcp_socket.recv(1024)
    print(ret.decode('gbk'))
    tcp_socket.close()
def server():#
    #创建套接字
    tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定端口
    tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    tcp_server.bind(('',8080))
    #监听端口
    tcp_server.listen()
    #接收信息
    data,address=tcp_server.accept()
    print(data)
    print(address)
    #控制大小和解码
    ret1=data.recv(1024)
    print(ret1.decode('gbk'))
def main():
    func1=threading.Thread(target=tcp_client)
    func2=threading.Thread(target=server)
    func1.start()
    func2.start()
if __name__ == '__main__':
    main()


