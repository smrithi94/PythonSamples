import random

scoreCounter=0
while True:
    firstNumber=random.randrange(1,10)
    secondNumber=random.randrange(1,10)
    correctAnswer=firstNumber+secondNumber
    question= 'what is: '+str(firstNumber)+ '+' +str(secondNumber)+'? '
    userAnswer=raw_input(question)
    userAnswer=int(userAnswer)

    if userAnswer == correctAnswer:
        print 'congratulations!! your answer is correct.'
        scoreCounter=scoreCounter+1

    else:
        print 'Sorry! Your answer was wrong. The right answer is',correctAnswer
        scoreCounter-=1

    userContinue=raw_input('Press N to exit.')
    if userContinue=='N':
        break
print 'Your score is',scoreCounter
