import socket
udp_socket=socket.socketsocket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST)
udp_socket.sendto('哈哈'.encode('gbk'),('255.255.255.255',9800))