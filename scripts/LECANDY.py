#LECANDY
# cook your dish here
test_cases = int(input())

for i in  range(test_cases):
    n,candy = map(int,input().split())
    elephant = (list(map(int,input().split())))
    s = sum(elephant)
    if s > candy :
        print('No')
    else :
        print('Yes')
