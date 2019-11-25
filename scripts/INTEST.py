#taking input
n, k = map(int, input().strip().split(' '))
count = 0
#count for each row
for i in range(n):
	x = int(input().strip())
	if x % k == 0:
	    count += 1
print(count)	