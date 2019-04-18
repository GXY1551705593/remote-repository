'''
1、创建socke套接字
2、需要使用bind来绑定端口
3、listen监听模式，等待接收用户的链接，使得套接字变成被动状态
4、accept处理用户链接
'''
import threading
import socket


def recv_data(service_client_socket):
    '''这个函数主要创建接收客户端的消息'''
    # 收消息
    try:
        while True:
            data = service_client_socket.recv(1024)

            if data:
                print(data.decode('gbk'))
            else:
                service_client_socket.close()
                break
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 1、套接字
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2、需要使用bind来绑定端口
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    server_socket.bind(("",8080))

    # 3、listen监听模式，等待接收用户的链接，使得套接字变成被动状态
    server_socket.listen()
    while True:
        # 主程序里面只是实现创建新的服务套接字
        service_client_socket,client_addressinfo = server_socket.accept()
        print(service_client_socket)
        print(client_addressinfo)

        # 服务套接字服务的过程扔给多线程取处理，此时并不影响主程序床架服务套接字
        recv_thread = threading.Thread(target=recv_data,args=(service_client_socket,))
        recv_thread.start()





