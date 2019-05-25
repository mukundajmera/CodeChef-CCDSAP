#LAPIN
# cook your dish here
test_cases = int(input())
for _ in range(test_cases):
    word = str(input())
    if len(word) % 2 != 0:
        first = list(word[:(len(word)//2)])
        second = list(word[(len(word)//2) +1:])
    else: 
        first = list(word[:(len(word)//2)])
        second = list(word[(len(word)//2):])
    if sorted(first) == sorted(second):
        print('YES')
    else:
        print('NO')

