'''描述下dict的items()方法和iteritems()方法的不同'''
dict={'age':25,'gender':'man'}
ret=dict.items()
dict.iteritems()
print(type(ret))
print(dict)
#items()方法和iteritems()方法,前者能在字典运行后者不能。