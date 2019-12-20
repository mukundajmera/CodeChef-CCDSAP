test_cases = int(input())
for _ in range(test_cases):
    num = str(input())
    if(num[::-1] == num[:]):
        print('wins')
    else:
        print('losses')

        
