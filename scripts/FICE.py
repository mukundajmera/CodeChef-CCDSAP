#FICE
# cook your dish here
test_cases = int(input())
f = []
f.append(0)
f.append(1)
for j in range(2,1001):
    f.append(f[j-1] + f[j-2])
for i  in range(test_cases):
    n,m = map(int,input().split())
    if n > 30 or m > pow(10,3):
        print(0)
        break
    print((2*f[n])%m)
    