#FLOW011
for _ in range(int(input())):
    n = int(input())
    sum = 0
    if(n < 1500):
        sum = n + n*.1 + n *.9
    else:
        sum = n + 500 + n *.98
    print("{0:.2f}".format(sum))