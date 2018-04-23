import random

rocks=0
papers=0
scissors=0
trials=0

maxTrials=raw_input('How many trials you want')
maxTrials=int(maxTrials)

while trials < maxTrials:

    rps=random.randrange(3)

    if rps==0:
        rocks=rocks+1
    if rps==1:
        papers=papers+1
    if rps==2:
        scissors=scissors+1
    trials=trials+1
print 'the number of rocks',rocks
print 'the number of papers',papers
print 'the number of scissors',scissors
