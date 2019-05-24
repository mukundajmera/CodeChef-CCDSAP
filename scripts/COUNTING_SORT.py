#input in range of 0 - 9
test_cases = int(input())
for i in range(test_cases):
	array1 = (list(map(int,input().split())))
	count = [0]*10
	#updating count
	for	i in array1:
		count[i] += 1 
	#updating overall count to update value 
	for j in range(1,len(count)):
		count[j] += count[j-1]	
	#traversing array1 to sort new list
	sorted_list = [0]*len(array1)
	for k in array1:
		sorted_list[count[k]-1] = k
		count[k] -= 1

	print(sorted_list)
