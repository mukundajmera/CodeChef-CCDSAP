#PRB01
import math
n = int(input())
flag = False
for _ in  range(n):
	num = int(input())
	flag = False
	for j in range(2,math.floor(math.sqrt(num))+1):
		if(num % j == 0):
		    flag = True
		    print('no')
		    break

	if(flag == False):
		print('yes')
