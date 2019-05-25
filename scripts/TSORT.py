#TSORT
# cook your dish here
def quick_sort(items,start,end):
	if start < end:
		p_index = partition(items,start,end)
		quick_sort(items,start,p_index-1)
		quick_sort(items,p_index+1,end)

def partition(items,start,end):
	#make partition of the smaller and bigger elements
	pivot = items[end]
	p_index = start
	for i in range(start,end):
		if items[i] <= pivot:
			items[i],items[p_index] = items[p_index],items[i]
			p_index += 1
	items[p_index],items[end] = items[end],items[p_index]
	return p_index

n = int(input())
items = []
for _ in range(n):
    items.append(int(input()))

quick_sort(items,0,len(items)-1)
for i in items:
    print(i)



# #TSORT
# # cook your dish here
# n = int(input())
# items = []
# for _ in range(n):
#     items.append(int(input()))

# items.sort()
# for i in items:
#     print(i)
