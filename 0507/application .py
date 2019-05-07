'''此文件实现的是应用程序框架'''

import time


# WSGI接口
def app(environ,start_response):
    '''

    :param environ: 跟HTTP请求相关的数据（用户的请求路径，用户的请求头），字典
    :param start_response:函数引用（由服务器提供），作用：设置状态和响应头
    start_reponse这个方法：设置状态和响应头，这个函数有两个参数，第一个参数表示状态，第二个表示响应的头部（类型：列表），写在服务器上，但是框架上调用
    :return:
    '''
    print('environ:',environ)
    request_path = environ['path']
    print(request_path)
    if request_path=='/gettime.py':

        # 调用服务器的方法，拼接响应头部信息
        start_response('200 ok',[('server','wsgisever'),('name','guazi'),('request_path',request_path)])
        # return 'hello world from WSGI'
        print(time.ctime())
        return time.ctime()

    else:
        '''处理动态资源匹配不到的问题 404 '''
        start_response('404 NOT FOUND', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        return '您请求的动态资源不存在'