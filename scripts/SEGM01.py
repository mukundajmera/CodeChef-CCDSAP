#SEGM01
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    str = list(input())
    valid = 0
    if str[0] == '1':
        valid += 1
    for i in range(len(str) -1):
        if(str[i] == "0" and str[i+1]=="1"):
            valid += 1
        if(valid > 1):
            break
    if(valid == 1):
        print("YES")
    else:
        print("NO")