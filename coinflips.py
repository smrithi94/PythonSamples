import random

nFlips=0
nHeads=0
nTails=0

maxFlips=raw_input('enter the maximum number of flips')
maxFlips=int(maxFlips)

while nFlips < maxFlips:
    zeroOne=random.randrange(2)
    if zeroOne==0:
        nTails=nTails+1
    elif zeroOne==1:
        nHeads=nHeads+1
    nFlips=nFlips+1
print 'The number of heads',nHeads
print 'The number of Tails',nTails 
