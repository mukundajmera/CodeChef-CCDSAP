#COPS
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    cops,x,y = map(int,input().split())
    loc = list(map(int,input().split()))
    multi = x * y
    remaining = list(range(1,101))
    seats = []
    for j in range(cops):
        sum = 0
        if (loc[j] - multi) > 0:
            min = loc[j] - multi
        else:
            min = 1
        if (loc[j] + multi) > 100:
            max = 100
        else:
            max = loc[j] + multi
        seats += list(range(min,max+1))
    remaining = set(remaining) - set(seats)
    print(len(remaining))        
    
    
    