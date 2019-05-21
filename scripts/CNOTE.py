#CNOTE
# cook your dish here
test_cases = int(input())
for i in  range(test_cases):
    x,y,k,n = map(int,input().split())
    req_pages = x - y
    output = 'UnluckyChef'
    for j in range(n):
        p = (list(map(int,input().split())))
        if  p[0] >= req_pages :
            if p[1] <= k:
                output = 'LuckyChef'
    print(output)            