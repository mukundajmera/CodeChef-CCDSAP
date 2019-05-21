#CSUB
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    str1 = str(input())
    carry = 0
    total = 0;
    for j in range(0,len(str1)):
        if str1[j] == '1' :
            total += 1
            total += carry
            carry += 1
    print(total)    