#CIELRCPT
# cook your dish here
test_cases = int(input())
array1 = [2048,1024,512,256,128,64,32,16,8,4,2,1]
for i in range(test_cases):
    n = int(input())
    menu = 0
    for j in array1:
        if(j <= n):
            while(n >= j):
                n = n -j
                menu += 1
        if(n == 0):
            break
    print(menu)