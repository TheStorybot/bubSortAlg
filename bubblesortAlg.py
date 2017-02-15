def bubbleSort (myList):
    for x in range (0, len(myList) - 1):
        for y in range(0, len(myList) - 1 - x):
            if myList[y] > myList[y + 1]:
                myList[y], myList[y+1] = myList[y+1], myList[y]
    return myList

myList = [67, 45, 2, 13, 1, 998]
bubbleSort (myList)
print (myList)
