#STRBIT
# cook your dish here
test_cases = int(input())
for _ in range(test_cases):
    n , k = map(int,input().split())
    str = input()
    memory = [0 for i in range(n+2)]
    count , check = 0 , 0
    for i in range(n):
        check += memory[i]
        if(not(check%2) and str[i]=='G') or 
        ((check)%2 and str[i] == 'R'):
            continue
        check += 1
        count += 1
        memory[min(n,i+k)] += 1
    print(count)