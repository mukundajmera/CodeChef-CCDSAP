#FRGTNLNG
# cook your dish here
test_cases = int(input())

for i  in range(test_cases):
    n,k = map(int,input().split())
    old_words = (list(map(str,input().split())))
    total_worlds = []
    for j in range(k):
        new_words = (list(map(str,input().split())))
        total_worlds += set(new_words[1:])
        
    for word in old_words:
        if word in total_worlds:
            print("YES",end=' ')
        else:
            print("NO",end=' ')
    print("")