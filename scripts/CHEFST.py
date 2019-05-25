#CHEFST
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    n1,n2,m = map(int,(input().split()))
    m = (m*(m+1))//2
    val = min(n1,n2,m)
    print(n1+n2-(2*val))