while(True):
    arr = int(input())
    if(arr == 0):
        break
    arr = [int(i) for i in input().split()]
    inv = [0]*len(arr)
    for i in arr:
        #fetch I position
        position = arr[i-1]
        #place it in new list
        inv[position-1] = i
    if(arr == inv):
        print('ambiguous')
    else:
        print('not ambiguous')