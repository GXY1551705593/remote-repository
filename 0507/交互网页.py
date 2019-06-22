import socket
import chardet
import multiprocessing
import sys
import pymysql

connect = pymysql.connect\
(host='localhost', port=3306,database='shuju',
 user='root', password='mysql', charset='utf8')
cur =connect.cursor()


class HttpServer(object):
    def __init__(self,port=8080):
        # 创建服务器套接字
        # 1、浏览器与服务器进行链接
        self.sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sever_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sever_socket.bind(('', port))
        self.sever_socket.listen()
        self.response_data = None # 响应报文的数据（除了响应体之外的内容）
        # self.connect = pymysql.connect(host='localhost', port=3306,database='shuju', user='root', password='mysql', charset='utf8')
        # self.cur = self.connect.cursor()


    def handler_client(self,client_server_socket):
        '''人工客服处理客户端的请求'''
        # 3、浏览器向服务器发送请求报文,服务器接收报文，报文是二进制
        data = client_server_socket.recv(1024).decode()
        list_data=data.split(' ')
        if list_data[0]=='POST':#获取用户名和密码
            str_user=str(list_data[-1])
            # 名字
            str_name = str_user[str_user.find('e=')+2:str_user.find('&')]
            print(str_name)
            # 密码
            str_password = str_user[str_user.find('d=') + 2:]
            print(str_password)
            inname=str_name
            inpassword=str_password
            #数据库操作
            sql_add='insert into infor values (0,%s,%s)'
            cur.execute(sql_add,[inname,inpassword])
            #上传到数据库
            connect.commit()
        ret_list = data.split('\r\n')

        #print(ret_list)
        # for obj in ret_list:
        #     #print(obj)
        #print('##############分割########################')
        # data是接收到的浏览器请求报文，并且是二进制文件，
        # 4、服务器根据浏览器发送的报文返回具体的响应
        # todo:  开始拼接的响应报文
        # todo:截取请求的路径，获取请求的具体内容，根据路径的不同，返回不同的数据
        # 4.0 获取请求报文的第一行，并且获取到路径
        request_first_line = ret_list[0]

        fistline_list = request_first_line.split(' ')
        #print(fistline_list[1])
        try:
            request_path = fistline_list[1]

        except:
            request_path = '/'
            print(request_path)
        # 根据路径，获取对应的数据
        if request_path == '/':#登录网页
            status_code = '200 ok'
            with open('login.html','r') as f:
                responsebody = f.read()
                #print(responsebody.decode())

        elif request_path == '/index.html':#登录后网页
            status_code = '200 ok'
            with open('index.html','r') as f:
                responsebody1 = f.read()
                list_sql=responsebody1.decode().split('<hr>')
                print('***************')
                #print(list_sql[1])
                sql='select * from infor'
                cur.execute(sql)
                ret_sql=str(cur.fetchall())
                responsebody=ret_sql.encode()
            print('***************')




        # 4.1 拼接第一行的数据HTTP/1.1 状态码 说明\r\n
        first_line = 'HTTP/1.1' + status_code + '\r\n'
        first_line += 'name:server\r\n'
        first_line += 'data:html\r\n'
        first_line += '\r\n'

        # 判断response的数据类型，进行和响应头的拼接，响应头是一个普通字符串
        try:
            chardet.detect(responsebody)
        except:
            response = first_line + responsebody
            response = response.encode('gbk')  # 凭借完成之后，直接编码
        else:
            # 说明试错语言没有问题，responsebody是一个二进制文件
            response = first_line.encode('gbk') + responsebody

        client_server_socket.send(response)
        # 5、人工客服完成任务之后被销毁
        client_server_socket.close()
        # 6、服务器套接字一般不会关闭
    def start(self):
        # 开始创建人工客服
        while True:
            # 2、在三次握手完成之后，为客户端套接字创建客服
            # accept 是指从三次握手完成的队列中取出客户端套接字，为他创建人工客服
            client_server_socket, addressinfo = self.sever_socket.accept()
            pro = multiprocessing.Process(target=self.handler_client, args=(client_server_socket,))
            pro.start()
    def start_response(self,status,header_list):
        response_header_firstline = 'HTTP/1.1 %s\r\n'%status
        reponse_header = ''
        for header_key,header_value in header_list:
            reponse_header += ('%s:%s\r\n'%(header_key,header_value))
        self.response_data = response_header_firstline + reponse_header + '\r\n'
def main():

    #print('此时获取的参数列表',sys.argv)
    try:
        # 获取命令行参数
        port = int(sys.argv[1])
    except:
        print('参数缺少')
        #return
        # 如果出现参数的获取失败问题，直接赋值默认值
        port = 8080
    finally:
        # 不管正确还是错误，都要进入的分支，启动服务器
        server_obj = HttpServer(port=port)
        server_obj.start()
if __name__ == '__main__':
    main()