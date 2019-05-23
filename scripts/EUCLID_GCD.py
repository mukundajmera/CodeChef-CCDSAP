#EUCLID_GCD
# input testcases line 1
# input number1 and number2 line 2
# output GCD

test_cases = int(input())
for i in  range(test_cases):
	a,b = map(int,input().split())
	divident = max(a,b)
	divisor = min(a,b)
	while divisor != 0 :
		remainder = divident % divisor
		divident = divisor
		divisor = remainder
	print(divident)
