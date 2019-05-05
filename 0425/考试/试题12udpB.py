import socket

def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    udp_socket.bind(("",9000))
    while True:
        data,address_info=udp_socket.recvfrom(1024)
        print('发送人：%s,信息是：%s'%(address_info,data.decode('gbk')))

    pass

if __name__ == '__main__':
    main()
