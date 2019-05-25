#SIMPSTAT
# cook your dish here
test_cases = int(input())
for _ in range(test_cases):
    n , k = map(int,input().split())
    array1 = list(map(int,input().split()))
    array1.sort()
    while(k > 0 ):
        array1.pop()
        array1.pop(0)
        k -= 1
    print(sum(array1)/len(array1))    