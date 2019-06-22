from rest_framework.views import exception_handler as drf_handler
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR



def exception_handler(exc, context):
    #如果框架能处理的异常，还是让框架处理
    response = drf_handler(exc,context)

    # 框架不能处理的异常，我们自己处理
    # if response is None:
    #     response = Response({'message':'服务器错误'},status=HTTP_500_INTERNAL_SERVER_ERROR)
    if response is None:
        # 项目出错了，但DRF框架对出错的异常没有处理,
        # 可以在此处对异常进行统一处理，比如：保存出错信息到日志文件
        view = context['view']  # 出错的视图
        error = '服务器内部错误, %s' % exc
        print('%s: %s' % (view, error))
        # return Response({'detail': error}, status=500)
        response = Response({'message': '服务器错误'}, status=HTTP_500_INTERNAL_SERVER_ERROR)


    return response

