import gevent
#monkey.pach_all()
class StaticServer():
    def createServer(self):
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        ss.bind(('', 9999))
        ss.listen(10)
        return ss

    def getrequest(self, ss):
        bs, ba = ss.accept()
        # 1024mb
        data = bs.recv(1024)
        # request_datas = data.splitlines()
        # for i in request_datas:
        #     # 响应体
        #     print(i)
        host = re.search('Host:.*\r', data.decode('gbk')).group()
        print(host)

        responseHeader = 'HTTP/1.1 200 get\r\n'
        responseHeader += '\r\n'
        if host == '/':
            responseBody = 'hello world!'.encode()
        elif host == '/index.html':
            with open('index.html') as f:
                response_data = f.read()
            responseBody = response_data
        elif host == '/login.html':
            with open(r'login.html', 'rb') as f:
                responseBody = f.read()
        elif host == '/tup.html':
            with open(r'tup.png', 'rb') as f:
                responseBody = f.read()
        else:
            with open(r'err.html', 'rb') as f:
                responseBody = f.read()
        response = responseHeader + responseBody
        bs.send(response.encode('gbk'))
        bs.close()

    def run(self):
        self.createServer()
        while True:
            # gr = threading.Thread(target=getrequest, args=(createServer(),))
            gr = multiprocessing.Process(target=getrequest, args=(createServer(),))
            gr.start()

if __name__ == '__main__':
    staticServer = StaticServer()
    staticServer.run()




