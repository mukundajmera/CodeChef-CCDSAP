test_cases = int(input())
for i  in range(test_cases):
	str1 = input()
	flag = False
	count = 0
	max1 = 0
	for i in str1:
		if i == '1':
			count += 1
		if i == '0':
			if count > max1:
				max1 = count
			count = 0

	if count > max1:
		max1 = count
	print(max1)
	# max1 = 0
	# count = 0
	# flag = False
	# for i in str1:
	# 	if i == '1' and flag == True:
	# 		count += 1
	# 	elif i == '0' and flag == True:
	# 		flag = False
	# 		if count > max1:
	# 			max1 = count
	# 		count = 0
	# 	elif i == '1' and flag == False:
	# 		count = 1
	# 		flag = True

	# if count > max1:
	# 	max1 = count

	# print(max1)

	# count = [len(i) for i in str1.split('0') if i != '']	
	# print(max(count))
