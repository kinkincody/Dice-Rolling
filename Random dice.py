import random as rd

again = str(input('Press enter to start dice rolling ')).upper()


while not again == 'NO':
    nd = int(input('How many dices you wanna roll? '))
        
    ndl = int(input('What is the smallest number of the dices? '))
    ndh = int(input('What is the largest number of the dices? '))
    count = 1
    
    for i in range(1, nd+1):
        dice = rd.randint(ndl, ndh)
        print(f'The number {count} roll: {dice}')
        count += 1
    
    again = str(input('Wanna roll again?')).upper()