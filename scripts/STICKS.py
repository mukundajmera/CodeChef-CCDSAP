#STICKS
# cook your dish here
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    array1 = (list(map(int,input().split())))
    array1.sort(reverse = True)
    i = 0
    selected = []
    while i < (len(array1)-1):
        if array1[i] == array1 [i+1]:
            selected.append(array1[i])
            i += 2
        elif len(selected) >= 2:
            break
        else:
            i += 1
    if(len(selected) >= 2 ):
       print(selected[0]*selected[1])
    else:
        print(-1)
