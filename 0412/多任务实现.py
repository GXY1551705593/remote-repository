
import threading
import socket

udp_socket = None


def send_conent():
    while True:
        sendinfo = input('请输入内容:')
        udp_socket.sendto(sendinfo.encode('gbk'),('192.168.44.1',8080))
def recv_connent():
    while True:
        data, address_info = udp_socket.recvfrom(1024)
        print('发送人:%s,接收的信息是：%s' % (address_info, data.decode('gbk')))

def func():


    global udp_socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("", 7000))


    send= threading.Thread(target=send_conent)
    recv= threading.Thread(target=recv_connent)

    send.start()
    recv.start()

    pass
if __name__ == '__main__':
    func()
