str='username=123456&userpassword=45566'
#名字

str_name=str[9:str.find('&')]
print(str_name)
#密码
str_password=str[str.find('d=')+2:]
print(str_password)