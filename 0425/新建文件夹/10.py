# 四.创建一个tcp服务器
# （1）能接收tcp客户端发来的请求
# 2）能并发处理客户端连接
# （3）能接收tcp客户端发来的数据、每次收到数据打印出来并dA回复客户端“已收到！谢谢！”、直到客户端主动断开（线程版）
import socket
import threading

tcp_socket = None


def socket_lianjie(fuwu_socket):
    global tcp_socket
    while True:
            data = fuwu_socket.recv(1024)
            tcp_socket.send('服务器已收到消息'.encode("utf-8"))
            if data:
                print(data.decode('utf-8'))
            else:
                break



if __name__ == '__main__':

    #1创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定ｉｐ
    tcp_socket.bind(('',8888))
    #搜索连接
    tcp_socket.listen()
    while True:
        fuwu_socket, add_socket = tcp_socket.accept()
        print(fuwu_socket)
        print(add_socket)

    tcp_thread = threading.Thread(target=socket_lianjie(),args=(fuwu_socket,))
    tcp_thread.start()



