#SALARY
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    workers = int(input())
    wage = (list(map(int,input().split())))
    diff = sum(wage) -(len(wage)* min(wage))
    print(diff)