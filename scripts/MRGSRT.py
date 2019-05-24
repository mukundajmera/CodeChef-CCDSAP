import math
# cook your dish here
def split_block(start,end,dept):
    mid = math.ceil((start + end + 1)/2)
    # print(' start ',start,' mid ',mid,' end ',end)
    global message 
    message += '{} {}\n'.format(start,end)
    global count
    count += 1
    if(mid > end):
        return
    if dept == start:
        split_block(start,mid-1,dept)
    else:
        split_block(mid,end,dept)
    
    
test_cases = int(input())
for i in range(test_cases):
    start,end,dept = map(int,input().split())
    count = 0
    message = ''
    split_block(start,end,dept)
    if count > dept:
        print(-1)
    else:
        print(message,end='')
        print(count)

    