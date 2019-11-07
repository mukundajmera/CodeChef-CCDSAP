#sum of the digits
test_cases = int(input())

#function for count
def DigitSum(num):
    count = 0
    for i in range(len(num)):
        count += int(num[i])
    return count

for _ in range(test_cases):
    num = input().strip()
    print(DigitSum(num))
