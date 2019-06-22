import random
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django_redis import get_redis_connection
from shanghuishop.libs.captcha.captcha import captcha

from . import constants
from . import serializers

# Create your views here.
class ImageView(APIView):
    def get(self,request,image_id):
        # 1、生成验证码
        text,image = captcha.generate_captcha()
        print('#################')
        print(text)
        # print(image)
        # 2、要保存验证码上面的文字部分
        # todo 2.1 连接校验专用的redis数据库
        redis_con_obj = get_redis_connection('valid')
        #todo 2.2 插入数据到redis，但是需要设置过期时间
        redis_con_obj.setex(image_id,constants.IMAGE_UUID_REDIS_EXPIRES,text)
        # setex(self, name, time, value)

        # 3、返回图片
        return HttpResponse(image,content_type='image/jpg')


class MsgView(GenericAPIView):
    serializer_class = serializers.ImageTextSerizers
    def get(self,request):
        # 1、校验图片验证码(当前已经由序列化器去实现)
        print('#################',request.query_params)
        #获取的是查询参数
        query_dict = request.query_params

        serializer=self.get_serializer(data=query_dict)
        # 获取serializer_class指定的序列化器对象，并且进行的序列化器的实例化
        serializer.is_valid(raise_exception=True)
        # print(serializer.errors)
        # 进行校验

        # 2、在5分钟不再重复发送 (利用redis可以设置过期时间的特点，将表示在5分钟内发送短信的标志设置放入redis)
        # redis中标志的例子 1311111111_flag:1
        # 3、生成短信验证码
        msg = '%04d'%random.randint(0,9999)
        print('生成的短信验证码',msg)

        # 4、保存短信验证码,并且，保存发送的状态，在5分钟
        # todo 2.1 连接校验专用的redis数据库
        redis_con_obj = get_redis_connection('valid')
        # todo 2.2 插入数据到redis，但是需要设置过期时间
        # todo 保存短信验证码，将来注册的时候需要进行比对
        # 获取手机号码
        # print('手机号码',query_dict['phone'])
        phone = query_dict['phone']
        redis_con_obj.setex('%s_msg'%phone,constants.PHONE_MSG_CODE_EXPIRES,msg)
        redis_con_obj.setex('%s_flag'%phone,constants.PHONE_FLAG_CODE_EXPIRES,msg)
        # setex(self, name, time, value)



        # 5、发送短信
        # 6、返回相应的响应数据
        return Response('ok')