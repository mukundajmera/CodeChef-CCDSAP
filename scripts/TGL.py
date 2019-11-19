rounds = int(input())
win = 1
max = 0
cum_A,cum_B = 0,0
for _ in range(rounds):
    scoreA,scoreB = list(map(int,input().strip().split(' ')))
    cum_A += scoreA
    cum_B += scoreB
    val = cum_A - cum_B
    if  val > 0 and abs(val) > max:
        max = abs(val)
        win = 1
    elif val < 0 and abs(val) > max:
        max = abs(val)
        win = 2
print(win,max)
    