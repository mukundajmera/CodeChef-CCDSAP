#AMR15A
n = int(input())
num = list(map(int,input().split()))
odd,even = 0,0
for i in range(n):
    if(num[i] % 2 == 0):
        even += 1
    else:
        odd += 1

if(even > odd):
    print('READY FOR BATTLE')
else:
    print('NOT READY')