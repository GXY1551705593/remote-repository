'''此文件实现的是应用程序框架'''

import time
import random


# WSGI接口

# 定义一个存放路径已经函数 映射的字典、
# urlfuncdict = dict()
urlfuncdict = {}
# {'index.py':indec,"login":login}


def route(url):
    print(url)
    def warpper(func):
        # 添加键值对，key:路径,vlaue:函数的引用
        urlfuncdict[url] = func
        print(urlfuncdict)
        def inner():
            response_body=func()
            return response_body
        return inner
    return warpper


@route('/login.py')
def login():
    '''用来处理登录的业务逻辑'''

    print('这是登录界面')
    return '返回的响应体数据是：这是登录界面'



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

    try:
        start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])

        reponse_body = urlfuncdict[request_path]()
        return reponse_body
    except:
        start_response('404 not', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        return '找不到'






