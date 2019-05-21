#COMPILER
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    expression = input()
    count = 0
    left = 0
    for j in range(len(expression)):
        if expression[j] == '<':
            left += 1
        else:
            left -= 1
        if left < 0:
            break
        if left == 0:
            count = j
    if count != 0:
        count += 1
    print(count)
    