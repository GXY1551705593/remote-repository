# 这个文件用来定义的是常量

#图片对应的uuid以及图片验证码对应的文字存储在redis的时间，单位是S
IMAGE_UUID_REDIS_EXPIRES = 60*60

#短信验证的存储时间5分
PHONE_MSG_CODE_EXPIRES = 5*60


#短信验证码标志的存储时间5分
PHONE_FLAG_CODE_EXPIRES = 1*60