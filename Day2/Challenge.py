def add(intlist, pos1, pos2, pos3):
    intlist[intlist[pos3]] = intlist[intlist[pos1]] + intlist[intlist[pos2]]

def multiply(intlist, pos1, pos2, pos3):
    intlist[intlist[pos3]] = intlist[intlist[pos1]] * intlist[intlist[pos2]]

def runIntCode(integerCode):
    for i in range(0, len(intCode), 4):
        if(integerCode[i] == 1):
            add(integerCode, i+1, i+2, i+3)
        elif(integerCode[i] == 2):
            multiply(integerCode, i+1, i+2, i+3)
        elif(integerCode[i] == 99):
            #print("Program Executed")
            break
    return integerCode

intCode = []

with open("input.txt") as txtFile:
    line = txtFile.read()
    intCode = line.strip("\n").split(",")

for i in range(0, len(intCode)):
    intCode[i] = int(intCode[i])

finalX = -1
finalY = -1

for x in range(0, 100):
    intCode[1] = x
    for y in range(0,100):
        intCode[2] = y
        copycode = intCode.copy()
        copycode = runIntCode(copycode)
        #print(intCode)
        #print(copycode)
        print("x =", x, "and y =", y)
        print(copycode[0])
        if copycode[0] == 19690720:
            finalX = x
            finalY = y
            break
    if finalX != -1:
        break

#print(intCode)
