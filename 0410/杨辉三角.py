n=int(input())
for i in range(n):
    for j in range(0, n-i):
        print(end=' ')
    for k in range(n-i,n):
        print("1",'2',end=" ",)

    print("")