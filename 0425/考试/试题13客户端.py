import socket
tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_socket.connect(('',9000))
while True:
    tcp_socket.send('你好'.encode('utf-8'))
    ret=tcp_socket.recv(1024)
    print(ret)