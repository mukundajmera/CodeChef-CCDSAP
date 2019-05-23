#CKISSHUG
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    m = 1000000007
    if n % 2 == 0:
        z=pow(2,n//2,m)
        z=3*z-2
    else:
        z=pow(2,(n+1)//2,m)
        z=(2*z -2)
    print(z%m)
    