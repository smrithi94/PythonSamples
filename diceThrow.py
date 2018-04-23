import random

def diceThrow():
    faceGot=random.randrange(1,7)
    return faceGot

countOfPairs=0

numberOfTries=raw_input('enter the number of rolls')
numberOfTries=int(numberOfTries)


for samePairs in range(numberOfTries):
    dice1=diceThrow()
    dice2=diceThrow()

    if dice1 == dice2:
        countOfPairs += 1

print numberOfTries,'throws gave',countOfPairs,'pairs'

print 'Thanks for trying!'

                  
