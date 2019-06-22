'''2、假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有200块钱，想买100只鸡，
计算有多少种买法，列出每一种买法？'''
list_ways=[]
for a in range(101):
    for b in range(101):
        c=100-a-b
        if 5*a+3*b+c==200:
            print([a,b,c],'第%s解法'%len(list_ways))
