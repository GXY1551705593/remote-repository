from rest_framework import serializers
from django_redis import get_redis_connection

class ImageTextSerizers(serializers.Serializer):
    image_id = serializers.UUIDField()
    image_text = serializers.CharField(max_length=4,min_length=4)
    phone = serializers.CharField(max_length=11,min_length=11)


    def validate(self, attrs):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(attrs)
        image_id_uuid = attrs['image_id']
        image_input_text = attrs['image_text']
        phone = attrs['phone']
        print(image_id_uuid)
        print(image_input_text)
        print(phone)

        # 验证用户输入的图片验证码的文字
        # todo 从redis数据库中取出正确的验证码文字
        redis_con_obj = get_redis_connection('valid')
        print(11111111111111111111)
        print(type(image_id_uuid))
        #'%s'%image_id_uuid 将uuid的类型数据，转成string
        correct_image_text = redis_con_obj.get('%s'%image_id_uuid)
        print(2222222222222222222222222)
        print('真正的验证码文字',correct_image_text)
        # 注意点从redis里面取出的数据是bytes类型的



        # todo 将用户输入的验证码与真实的验证码对比
        correct_image_text = correct_image_text.decode()
        if correct_image_text.lower() != image_input_text.lower():
            raise serializers.ValidationError('验证码错误')


        # todo 取出该手机号码对应的发送标志，如果能取到，说明已经在5分钟内发送过了
        flag = redis_con_obj.get('%s_flag'%phone)
        if flag:
            raise  serializers.ValidationError('在5分钟内请勿重复发送')



        return attrs
