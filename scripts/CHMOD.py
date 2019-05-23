#CHMOD
# cook your dish here
n =  int(input())
array1 = (list(map(int,input().split())))
for _ in range(int(input())):
    start,end,modulo = map(int,input().split())
    multi = 1
    # print('start ',start,' end ',end)
    for i in range(start,end+1):
        # print(array1[i-1])
        multi = multi*array1[i-1]
    print(multi%modulo)
