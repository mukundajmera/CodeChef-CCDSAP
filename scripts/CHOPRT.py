test_cases = int(input())
for _ in range(test_cases):
    a,b = map(int,input().strip().split(' '))
    if(a == b):
        print('=')
    elif(a < b):
        print('<')
    else:
        print('>')