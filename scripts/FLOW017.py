test_cases = int(input())
for _ in range(test_cases):
    x = list(map(int,input().strip().split(' ')))
    x.sort()
    print(x[1])