'''此文件实现的是应用程序框架'''

# WSGI接口
def app(environ, start_response):
    """
    :param environ: 跟HTTP请求相关的数据（用户的请求路径，用户的请求头），字典
    :param start_response:函数引用（由服务器提供），作用：设置状态和响应头
    start_reponse这个方法：设置状态和响应头，这个函数有两个参数，第一个参数表示状态，第二个表示响应的头部（类型：列表），写在服务器上，但是框架上调用
    :return:
    """
    print('environ:', environ)
    path = environ['path']
    if path == '/temp.py':
        start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi')])
        print("aaaaaaaaaaaaaaaaaaaaaaaaa")
        with open('temp.html',encoding='utf-8') as f:
            response = f.read()
            return response
