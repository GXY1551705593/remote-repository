# coding:utf-8
'''这个程序实现的是一个静态服务器'''
import socket
import re
import sys


def main(port):
    '''主函数，实现逻辑'''
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', port))

    server_socket.listen()
    while True:
        handler_socket, address = server_socket.accept()
        data = handler_socket.recv(1024).decode()  # 字节流文件--字符串
        print(data)
        request_datas_list = data.split('\r\n')
        print(request_datas_list)
        first_line = request_datas_list[0]
        ret = re.search('GET (/.*?) HTTP/1.1', first_line)
        # 判断是否有ret值，如果没有，说明是一个非法请求
        if not ret:
            handler_socket.close()
            return
        request_path = ret.group(1)

        print('**********************')

        '''
        HTTP/1.1 状态码 说明\r\n
        Headername1:header_value\r\n
        Headername2:header_value\r\n
        Headername3:header_value\r\n
        \r\n
        Response_body 响应体，就是数据，网页、图片、文本
        '''
        responseHeader = 'HTTP/1.1 200 ok123\r\n'
        responseHeader += '\r\n'
        if request_path == '/':
            responsebody = 'hello world!'
            reponse = (responseHeader + responsebody).encode()
        elif request_path == '/index.html':
            responseHeader = responseHeader.encode()
            with open('index.html') as f:
                reponse = responseHeader + f.read().encode()
        elif request_path == '/login.html':
            responseHeader = responseHeader.encode()
            with open('123.PNG', 'rb') as f:
                reponse = responseHeader + f.read()

        else:
            responseHeader = responseHeader.encode()
            with open('err.html') as f:
                reponse = responseHeader + f.read().encode()

        # ~ reponse = responseHeader+responsebody
        l_reponse = len(reponse)
        n_reponse = 0
        a = 0
        b = 3
        # ~ handler_socket.send(reponse[a:b])
        # ~ c=handler_socket.send(reponse)
        # ~ print(c)
        while n_reponse < l_reponse:
            c = handler_socket.send(reponse[a:b])
            a = b
            b += 3
            print(c)


if __name__ == '__main__':
    print(sys.argv[1])
    main(int(sys.argv[1]))
