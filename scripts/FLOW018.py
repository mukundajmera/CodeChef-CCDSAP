test_cases = int(input())
def fact(num):
    if(num <= 1):
        return 1
    return (num * fact(num-1))
for _ in range(test_cases):
    num = int(input())
    print(fact(num))