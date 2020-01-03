#FLOW010
for _ in range(int(input())):
    choice = str(input()).lower()
    if(choice == 'b'):
        print('BattleShip')
    elif(choice.lower() == 'c'):
        print('Cruiser')
    elif(choice.lower() == 'd'):
        print('Destroyer')
    elif(choice.lower() == 'f'):
        print('Frigate')
