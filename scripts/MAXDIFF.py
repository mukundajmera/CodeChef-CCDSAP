#MAXDIFF
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    n,k = map(int,(input().split()))
    array1 = list(map(int,input().split()))
    chef = 0 #chief
    son = 0 #son
    if(k > int(n/2)):
        array1.sort(reverse=True)
        chef = sum(array1[:k]) #chef
        son = sum(array1[k:]) #son
    else:
        array1.sort()
        son = sum(array1[:k]) #son
        chef = sum(array1[k:]) #chef
    print(chef - son)    