'''异常嵌套文件，找到文件时打开：未找到时，就报错'''
try:
    g=open('说明.txt')
    try:
        ret=g.readlines()
        print(ret)
    finally:
        g.close()
        print('该文件已关闭')
except FileNotFoundError:
    print('文件未找到')
except UnicodeEncodeError:
    print('文件编码错误')
