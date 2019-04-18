'''聊天系统'''
import socket
def func():
    udp_sockt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_sockt.bind(('',6000))
    conent = input('请输入内容：')

    while True:

        udp_sockt.sendto(conent.encode('gbk'), ('', 9800))
        data,adress=udp_sockt.recvfrom(1024)
        print('发送人：%s，接收信息是：%s'%(adress,data.decode('gbk')))
if __name__=='__main__':
    func()
