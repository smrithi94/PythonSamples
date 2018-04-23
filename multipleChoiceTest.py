from mulChoiceFile import *

DATA_FILE_PATH='mulquiz.txt'
LETTERS_LIST=['a','b','c','d']

fileHandle=openFileForReadiing(DATA_FILE_PATH)
titleText=readLine(fileHandle)
nQuestions=readLine(fileHandle)
nQuestions=int(nQuestions)

print 'Welcome!This test is'
print
print titleText
print 'There will be',nQuestions,'questions.'
print
print "Let's go"
print

score=0
for questionNumber in range(0,nQuestions):
    questionsText=readLine(fileHandle)
    answers=[]
    for i in range (0,4):
        thisAnswer=readLine(fileHandle)
        answer.append(thisAnswer)

    correctAnswer=answers[0]
    random.shuffle(answers)
    indexOfCorrectAnswer=answers.index(correctAnswer)

    print
    print str(questionNumber+1)+'.'+questionText
    for index in range(0,4):
        thisLetter=LETTER_LIST[index]
        thisAnswer=answers[index]
        thisAnswerLine=''+thisLetter+')'+thisAnswer
        print thisAnswerLine
    
