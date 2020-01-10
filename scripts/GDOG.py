#GDOG
for _ in range(int(input())):
    n,k = map(int,input().split())
    res = -1
    for i in range(1, k+1):
        if(n%i > res):
            res = n%i
    print(res)