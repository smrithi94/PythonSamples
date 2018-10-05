import random

def chooseAtRandom(myList):
    nLength=len(myList)
    nElement=random.randrange(0,nLength)
    element= myList[nElement]
    return element

nounList=['vijay','manu','vimitha','prashanth','tara','swathi','nila','dhivya','siva']
verbList=['sings','dances','eats','cooks','sleeps','runs']
adjectiveList=['smart','sweet','bad','worse','great']
    

while True:

    noun=chooseAtRandom(nounList)
    verb=chooseAtRandom(verbList)
    adjective=chooseAtRandom(adjectiveList)
    print noun +' ' +verb +' '+adjective
    print
    goAgain =raw_input('Press ENTER to continue or press(Q/q) to quit ')
    if goAgain=='q' or goAgain=='Q':
        break

print 'Thanks for playing'
            

