class Framework(object):
    def __init__(self):
        pass
    def __call__(self, environ,start_response):
        print('environ:', environ)
        path = environ['path']
        for path,func in urlfunclist:
            if path == '/temp.py':
                start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi')])
                print("aaaaaaaaaaaaaaaaaaaaaaaaa")
                with open('index.html', encoding='utf-8') as f:
                    response = f.read()
                    return response
