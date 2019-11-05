#test cases
test_case = int(input().strip())
#recursive function
def fact(num):
    if num == 1:
        return 1
    return (num* fact(num-1))
    
for _ in range(test_case):
    num = int(input())
    print(fact(num))
