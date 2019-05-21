# your code goes here
test_cases = int(input())
for i in range(test_cases):
	n = int(input())
	array1 = (list(map(int,input().split())))
	d1 = 0
	d1_pos = 0
	d2 = 0
	array2 = array1[::-1]
	# print(array2)
	for j in range(len(array2)-1):
		# print(array2[j])
		if array2[j] > array2[j+1]:
			d1 = array2[j+1]
			d1_pos = (n + j)%n #reverse position
			break
	# print("value of d1 ",d1," value of d1_pos ",d1_pos)
	if d1 == 0:
		print(-1)
	else:
		# print('array1[k] ',array1)
		for k in range(d1_pos,n):
			# print('d1 ',d1,'array1[k] ',array1[k])
			if d1 > array1[k]:
				d2 = array1[k-1]
				# print(d2)
				array1[k-1],array1[d1_pos-1] =  array1[d1_pos-1],array1[k-1]
				array1 = array1[0:d1_pos] + sorted(array1[d1_pos:n])
				print(array1)
				break;
		