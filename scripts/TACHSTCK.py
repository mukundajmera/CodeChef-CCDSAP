#TACHSTCK
# cook your dish here
n , d = map(int,input().split())
if(n == 1):
    print(0)
else:
    sticks = [int(input()) for i  in range(n)]
    sticks.sort()
    count = 0
    itr = 0
    while(itr < n-1):
        if sticks[itr+1] - sticks[itr] <= d :
            count += 1
            itr += 2
        else:
            itr += 1
    print(count)