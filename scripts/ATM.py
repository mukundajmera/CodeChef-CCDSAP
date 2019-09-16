withdraw,bal = list(map(float,input().strip().split(' ')))
#check for multiple and check for sum
if(withdraw%5 == 0  and ((withdraw + 0.5) <= bal)):
    print("{0:.2f}".format(bal - withdraw - 0.5))
else:
    print("{0:.2f}".format(bal))
