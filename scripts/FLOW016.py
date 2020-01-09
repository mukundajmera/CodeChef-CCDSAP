#FLOW016
import math
for _ in range(int(input())):
    num1,num2 = map(int,input().split())
    gcd = math.gcd(num1,num2)
    lcm = int((num1 * num2) / gcd)
    print(gcd,lcm)