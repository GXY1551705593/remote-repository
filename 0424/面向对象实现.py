import socket
import sys

class Socket():
    def __init__(self,port):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("", self.port))
        self.server_socket.listen(5)
        self.reponse_data=None
    def creat(self,c_s_socket):
        while True:
            # 2.在三次握手完成后，为客户端套接字创建客服
            c_s_socket, addressinfo = self.server_socket.accept()
            # self.handler(c_s_socket)
            # 3.浏览器向服务器发送请求报文,服务器接收报文

            data = c_s_socket.recv(1024).decode()
            # print(data)
            # data是接收到的浏览器请求报文,并且是二进制文件
            ret = data.split("\r\n")
            for i in ret:
                print(i)

            # 4.服务器根据浏览器发送的报文返回具体响应
            # todo:开始拼接响应报文
            # todo:截取请求的路径，获取请求的具体内容，根据路径不同，返回不同数据
            # 4.0获取请求报文第一行
            request_first_line = ret[0]
            ret2 = request_first_line.split(' ')
            print(ret2)
            try:
                request_path = ret2[1]
            except:
                request_path = '/index'
            # 根据路径，获得对应数据
            if request_path == '/index':
                status = '200 ok'
                with open('index.html', 'rb') as f:
                    responsebody = f.read()
            elif request_path == '/login':
                status = '200 ok'
                with open('a.jpg', 'rb') as f:
                    responsebody = f.read()
            else:
                status = '404 not found'
                with open('err.html', 'rb')as f:
                    responsebody = f.read()

            # 4.1拼接第一行的数据HTTP/1.1 状态码 说明\r\n
            first_line = 'HTTP/1.1' + status + '\r\n'
            first_line += 'name:server\r\n'
            first_line += '\r\n'
            # responsebody='hello world!'
            response = first_line.encode('GBK') + responsebody
            c_s_socket.send(response)

            # 5.人工客服完成任务之后被销毁
            c_s_socket.close()
            # 6.服务器套接字一把那不会关闭

    def start_response(self,status,header_list):
        '''
        这个函数实现的是拼接响应报文，遵循的还是响应报文的格式，请求动态资源的时候调用
        :param status: 状态码。例如：‘200 ok’
        :param header_list: 列表，例如：[(server,wsgiserver)，(name,guazi)]
        :return:
        '''
        response_header_fl = ' HTTP/1.1 %s \r\n'%status
        response_header=''
        for header_key,header_value in header_list:
            response_header+=('%s:%s\r\n'%(header_key,header_value))
        self.reponse_data = response_header_fl + response_header+'\r\n'
if __name__ == '__main__':

    try:
        port = int(sys.argv[1])
    except:
        port = 8080
    finally:
        socket_obj = Socket(port)
        socket_obj.creat(socket_obj)
