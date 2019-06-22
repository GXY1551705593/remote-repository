'''思维导图转换'''
def csv2json():
    with open('history.csv','r',encoding='UTF-8-sig') as f:
        doc=f.read()
        #doc.split(',')
        ret=doc.split(',')
        print(ret)
        print(ret[ret.index('金字塔\n')].split())
        list_africa=[]
        list_africa.append(ret[ret.index('古埃及文明')])
        list_africa.append(ret[ret.index('金字塔\n')].split())
        print(list_africa)
        list_asian=[]
        list_asian1=[]
        list_asian2=[]
        list_asian.append(ret[ret.index('两河流域文明')])
        list_asian.append(ret[ret.index('古印度')])
        list_asian1.append(ret[ret.index('汉谟拉比法典\n')])
        list_asian1.append(ret[ret.index('种姓制度\n')])
        list_asian1.append(ret[ret.index('佛教的创立\n')])
        print(list_asian)
        print(list_asian1)
        list_europe=[]
        list_europe3=[]
        list_europe.append(ret[ret.index('希腊')])
        list_europe.append(ret[ret.index('罗马')])
        list_europe.append(ret[ret.index('希腊罗马古典文化')])
        print(list_europe)
        #print(doc.index('奴隶社会','非洲','古埃及文明'))




csv2json()