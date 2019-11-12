test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    count = 0
    while(num > 0):
        if(num % 10 == 4):
            count += 1
        num = int(num / 10)
    print(count)
