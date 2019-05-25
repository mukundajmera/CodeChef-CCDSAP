#SUBINC
# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=[int(x) for x in input().split()]
    s=n 
    p=0
    for j in range(1,n):
        if l[j]>=l[j-1]:
            p+=1 
            s+=p 
        else:
            p=0
    print(s)