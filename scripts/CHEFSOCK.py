#CHEFSOCK
# cook your dish here
jacket_cost,sock_cost,money = map(int,input().split())
money -= jacket_cost
number_of_socks = money // sock_cost
if(number_of_socks % 2 == 0):
    print("Lucky Chef")
else:
    print("Unlucky Chef")