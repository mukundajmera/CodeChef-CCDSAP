test_cases = int(input())
for _ in range(test_cases):
    num = int(input())
    rev = 0
    while(num > 0):
        rev *= 10
        digit = num % 10
        rev += digit
        num = int(num / 10)
    print(rev)
    