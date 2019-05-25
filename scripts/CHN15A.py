#CHN15A
# cook your dish here
test_cases = int(input())
for _ in range(test_cases):
    n , coff = map(int,input().split())
    array1 = (list(map(int,input().split())))
    count = 0
    for i in array1:
        if((i + coff)%7 == 0):
            count += 1
    print(count)