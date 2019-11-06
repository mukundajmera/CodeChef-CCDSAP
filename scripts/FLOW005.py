test_cases = int(input())
arr = [100,50,10,5,2,1]
for _ in range(test_cases):
    num = int(input())
    count = 0
    for i in arr:
        count += int(num // i)
        num = num % i
    print(count)
