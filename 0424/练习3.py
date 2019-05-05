import socket
import sys
import chardet
import multiprocessing
class HttpServer(object):
    def __init__(self,port=8080):
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.server_socket.bind(('',port))
        self.server_socket.listen()
        self.response_data=None
    def hangdler_client(self,client_server_socket):
        data=client_server_socket.recv(1024).decode()
        ret_list=data.split('\r\n')
        requst_first_line=ret_list[0]
        firstline_list=requst_first_line.split('')
        try:
            requst_path=firstline_list[1]
        except:
            requst_path='/'
        if requst_path=='/':
            statue_code='200 ok'
            with open('index.html')as f:
                resonsebody=f.read()
        else:
            statue_code='404 not found'
            with open('err.html')as f:
                resonsebody=f.read()
        first_line='Http/1.1'+statue_code+'\r\n'
        first_line='name:serve\r\n'
        first_line='data.html\r\n'
        try:
            chardet.detect(resonsebody)
        except:
            response=first_line+resonsebody
            response=response.encode('gbk')
        else:
            response=first_line.encode()+resonsebody
        client_server_socket.send(response)
        client_server_socket.close()
    def start(self):
        while True:
            client_server_socket,addressinfo=self.server_socket.accept()
            pro=multiprocessing.Process(target=self.hangdler_client(),args=(client_server_socket,))
            pro.start()
    def start_response(self,status,header_list):
        response_header_firstline='Http/1.1%s\r\n'%status
        response_header=''
        for header_key,header_value in header_list:
            response_header+=('%s%s\r\n'%(header_key,header_value))
        self.response_data=response_header_firstline+response_header+'\r\n'
def main():
    print('此时获得参数列表',sys.argv)
    try:
        port=int(sys.argv[1])
    except:
        print('参数较少')
        port=8080
    finally:
        server_obj=HttpServer(port=port)
        server_obj.start()
if __name__ == '__main__':
    main()












