#PPSUM
def sumP(D, N):
    if(D == 1):
        return (N*(N+1))/2
    else:
        val = sumP(D-1, N)
        return (val*(val+1))/2 

for _ in range(int(input())):
    D, N = list(map(int, input().split()))
    print(int(sumP(D, N)))
