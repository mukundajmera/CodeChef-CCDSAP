#FLOW014
for _ in range(int(input())):
    h,c,t = map(str,input().split())
    h,c,t = int(h),float(c),int(t)
    if(h > 50 and c < .7 and t > 5600):
        print(10)
    elif(h > 50 and c < .7):
        print(9)
    elif(c < .7 and t > 5600):
        print(8)
    elif(h > 50 and t > 5600):
        print(7)
    elif(h > 50 or c < .7 or t > 5600):
        print(6)
    elif(not(h > 50 or c < .7 or t > 5600)):
        print(5)
