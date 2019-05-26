#RESQ
import math
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    n =  int(input())
    fact1 = int(math.sqrt(n))
    while(fact1 > 0):
        if(n%fact1 == 0):
            fact2 = n//fact1
            print(fact2 - fact1)
            break
        fact1 -= 1