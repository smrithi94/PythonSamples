N = raw_input('Enter the maximum range')
N=int(N)
listNumber=[]
for element in range(0, N):
    insertNumber=raw_input('Enter your list elements')
    insertNumber=int(insertNumber)
    listNumber.append(insertNumber)
print listNumber
listNumber.insert(2,6)
print listNumber 

elementToDelete=raw_input('Element you want to delete')
listNumber.remove(6)
print listNumber
print 'sorted list'
listNumber.sort()
print listNumber
print 'reversed list'
listNumber.sort(reverse=True)
print listNumber
