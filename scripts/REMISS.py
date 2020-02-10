test_cases = int(input())
for _ in  range(test_cases):
    a,b = map(int,input().strip().split(' '))
    #give max in firxt of 2 numbers, give sum for maximun Chefs
    print(max(a,b),a+b)