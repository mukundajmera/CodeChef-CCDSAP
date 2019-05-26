#MANYCHEF
# cook your dish here
test_cases = int(input())
for i  in range(test_cases):
    str = list(input())
    n = len(str)
    for i in range(len(str)-3):
        if((str[n-i-4] == '?' or str[n-i-4]=="C") 
        and (str[n-i-3] == '?' or str[n-i-3]=="H")
        and (str[n-i-2] == '?' or str[n-i-2]=="E")
        and (str[n-i-1] == '?' or str[n-i-1]=="F")):
            str[n-i-4] = "C"
            str[n-i-3] = "H"
            str[n-i-2] = "E"
            str[n-i-1] = "F"
            # i += 3
    final = ""
    final = final.join(str).replace("?","A")
    print(final)