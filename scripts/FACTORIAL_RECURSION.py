#FACTORIAL
# INPUT
# number of test cases  line 1
# each test case number line 2 to n
def fact(n):
	if n < 2:
		return 1;
	return (n * fact(n -1))

test_cases = int(input())
for i in range(test_cases):
	n = int(input())
	answer = fact(n)
	# while(n >= 1):
	# 	answer *= n
	# 	n -= 1
	print(answer)


