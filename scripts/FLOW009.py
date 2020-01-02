#FLOW009
for _ in range(int(input())):
    inputData = list(map(int,(input().split())))
    qty,price = inputData[0],inputData[1]
    if(qty <= 1000):
        print("{0:.6f}".format(price * qty))
    else:
        print("{0:.6f}".format(price * qty * .9))