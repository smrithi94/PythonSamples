userNumber=raw_input('enter the number')
userNumber=int(userNumber)
highEnd=userNumber+1
total=0
for numbers in range(0,highEnd):
    total=total+numbers
print total
