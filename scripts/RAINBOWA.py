#RAINBOW
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    n =  int(input())
    rainbow = (list(map(int,input().split())))
    output = 'yes'
    if rainbow != rainbow[::-1] or set(rainbow) != set([1,2,3,4,5,6,7]):
       output = 'no'
    print(output)
        