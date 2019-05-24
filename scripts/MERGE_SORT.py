#Mergsort
def mergesort(left,right):
	#merging using mergesort function
	i, j = 0, 0
	n = []
	while(i < len(left) and j < len(right) ):
		if(left[i] <= right[j]):
			n.append(left[i]) 
			i += 1
		else:
			n.append(right[j])
			j += 1
	n.extend(left[i:])
	n.extend(right[j:])
	return n



def merge(n):
	if len(n) < 2:
		return
	mid = len(n)//2
	left = n[:mid]
	right = n[mid:]
	merge(left)
	merge(right)
	return mergesort(left,right)

abc = [1,6,2,8]
print(merge(abc))
