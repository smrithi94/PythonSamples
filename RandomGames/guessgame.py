import random
MAX_GUESSES=5
MAX_RANGE=20

def guessTheNumber():
    print'Guess game'
    print 'You can guess a number between 1 and',MAX_RANGE
    print 'You have maximum of',MAX_GUESSES,'guesses.'

    

    guessCounter=0

    while True:
        inputNumber=raw_input('Enter the number : ')
        inputNumber=int(inputNumber)
        guessCounter=guessCounter+1

        target=random.randrange(1,MAX_RANGE +1)

        if guessCounter == MAX_GUESSES:
            print 'sorry yout trial limit reached'
            break

        if target== inputNumber:
            print 'Congratulations!!You have found out the number in' ,guessCounter,'guess(es)'

            break            

        elif target< inputNumber:
            print'Your number is too high for the target'

        elif target>inputNumber:
            print'Your number is too low for the target'
            
        
while True:
    guessTheNumber()

    tryAgain=raw_input('Do you want to continue? ')
    if tryAgain=='n'or tryAgain=='N':
        break
print 'thanks'


        
