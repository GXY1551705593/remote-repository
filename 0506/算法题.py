''''a+b+c=1000,a^2+b^2=c^2,求a，b，c'''
for b in range(1000):
    for c in range(1000):
        a=1000-b-c
        if a**2+b**2==c**2 and a>0 and b>0 and c >0:
            print(a,b,c)
