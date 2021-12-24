import random
numberOfStreaks = 0
ResultofFlips = []

for experimentNumber in range(10000):
    streak = 0
    for i in range(100):
        possible = ['H','T']
        ResultofFlips.append(possible[random.randint(0,1)])
    
    
    for k in range(len(ResultofFlips)):
        if ResultofFlips[k] == ResultofFlips[k-1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1
     
print('Chance of streak: %s%%' % (numberOfStreaks / 100))