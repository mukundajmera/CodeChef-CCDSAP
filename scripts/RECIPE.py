import os
import sys
from math import factorial
from fractions import gcd
def findHCF(a,b):
    numA,numB = 0,0
    if(a > b):
        numA = a
        numB = b
    else:
        numA = a
        numB = b
        rem =  sys.maxsize
    while(rem > 1):
        qot = numA // numB
        rem = numA % numB
        numA = numB
        if(rem == 0):
            break;
        numB = rem
    return numB

#execution of program
test_cases = int(input())
for _ in range(test_cases):
    arr = list(map(int,input().split()))
    gc = arr[1]
    for i in range(1,len(arr)):
        gc = gcd(gc,arr[i])
        if gc==1:
            break;
    arr = [x//gc for x in arr]
    print(" ".join(list(map(str,arr[1:]))))
