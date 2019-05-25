#input enter the n number of n elements line 1
#input enter all element in one line seprating with the space (sorted)
#end the element to be find

n = int(input())
array1 = (list(map(int,input().split()))) 
element = int(input())
start = 0;
end = len(array1)-1
position = -1
while(start <= end):
	mid = (start + end) // 2
	if(array1[mid] == element):
		position = mid
		break
	#first half
	if(array1[mid] > element):
		end = mid - 1
	#second half
	elif(array1[mid]< element):
		start = mid + 1
print(position)