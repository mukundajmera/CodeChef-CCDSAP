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

# cook your dish here
# test_cases = int(input())
# for _ in range(test_cases):
#     n = int(input())
#     digits = list(str(input()))
#     coff,count = 0,0
#     for i in range(len(digits)):
#         if(digits[i] == '1'):
#             count += 1 + coff
#             coff += 1
#     print(count)