import math
import re
import numpy as np

f = open("example.in")
fw = open("1example.txt", 'w+')

numberOfRows = 0    # R
numberOfColumns = 0 # C
L = 0   # at least L mushrooms & tomatos
H = 0   # at most of both mushrooms & tomatos

first_line = f.readline()
numbers = first_line.split()

numberOfRows = int(numbers[0])
numberOfColumns = int(numbers[1])
L = int(numbers[2])
H = int(numbers[3])

validSlices = []    # array to hold all valid slices with thier coordinates

pizza = np.zeros((numberOfRows, numberOfColumns)) #init the 2-D array

# read the file and put data in the array
i = 0
for line in f:
    j = 0
    for cell in line:
        if cell == 'T':
            pizza[i][j] = 0
        elif cell == 'M':
            pizza[i][j] = 1
        j += 1
    i += 1

print(pizza)
        
class PizzaSlice:
    def __init__(self, r1, r2, c1, c2):
        self.r1 = r1
        self.r2 = r2
        self.c1 = c1
        self.c2 = c2

def checkIfCorrectSlice(aSlice):
    totalM = 0
    totalT = 0

    for x in xrange(0, len(aSlice)):
        if aSlice[x] == 0:
            totalT += 1
        else:
            totalM += 1
        pass
    
    if totalM >= L and totalT >= L and (totalM + totalT) <= H:
        return True
    else:
        return False
    pass


for y in xrange(0, numberOfColumns):
    aSlice = [] # re-create the slice (only 1 column slice at the moment)
    r1 = 0
    continueLooking = False
    lastSlice = PizzaSlice(0,0,0,0)
    for x in xrange(0, numberOfRows):
        aSlice.append(pizza[x][y])  # append cell to slice
        isItCorrent = checkIfCorrectSlice(aSlice)

        if isItCorrent:
            continueLooking = True
            lastSlice = PizzaSlice(r1 = r1, r2 = x, c1 = y, c2 = y)

        if not isItCorrent and continueLooking:
            continueLooking = False
            validSlices.append(lastSlice)
            aSlice = [] # reset the slice
            aSlice.append(pizza[x][y])  # append cell to slice
            r1 = x + 1

        if isItCorrent and x == numberOfRows-1:
            pizzaSlice = PizzaSlice(r1 = r1, r2 = x, c1 = y, c2 = y)
            validSlices.append(pizzaSlice)

        if len(aSlice) == H:
            aSlice = [] # reset
            r1 = x + 1

            if continueLooking:
                continueLooking = False
                validSlices.append(lastSlice)

    pass 
pass


fw.write(str(len(validSlices)))
fw.write('\n')
for x in xrange(0, len(validSlices)):
    r1 = validSlices[x].r1
    r2 = validSlices[x].r2
    c1 = validSlices[x].c1
    c2 = validSlices[x].c2
    fw.write('{0} {1} {2} {3}'.format(r1, c1, r2, c2))
    fw.write('\n')
    pass

f.close()
fw.close()