def add(code, para1, mode1, para2, mode2, para3, mode3, relaIndex):
    if mode1 == 0:
        para1 = code[para1]
    elif mode1 == 2:
        para1 = code[para1 + relaIndex]
    if mode2 == 0:
        para2 = code[para2]
    elif mode2 == 2:
        para2 = code[para2 + relaIndex]
    if mode3 == 2:
        para3 = para3 + relaIndex
    code[para3] = int(para1) + int(para2)

def multiply(code, para1, mode1, para2, mode2, para3, mode3, relaIndex):
    if mode1 == 0:
        para1 = code[para1]
    elif mode1 == 2:
        para1 = code[para1 + relaIndex]
    if mode2 == 0:
        para2 = code[para2]
    elif mode2 == 2:
        para2 = code[para2 + relaIndex]
    if mode3 == 2:
        para3 = para3 + relaIndex
    code[para3] = int(para1) * int(para2)

def inputOp(code, para1, mode1, relaIndex):
    if mode1 == 2:
        code[para1 + relaIndex] = input("Enter Input:")
    else:
        code[para1] = input("Enter Input:")
    
def outputOp(code, para1, mode1, relaIndex):
    if mode1 == 0:
        para1 = code[para1]
    elif mode1 == 2:
        para1 = code[para1 + relaIndex]
    print(para1)

def jumpIfTrue(code, index, para1, mode1, para2, mode2, relaIndex):
    if mode1 == 0:
        para1 = code[para1]
    elif mode1 == 2:
        para1 = code[para1 + relaIndex]
    if mode2 == 0:
        para2 = code[para2]
    elif mode2 ==2:
        para2 = code[para2+ relaIndex]
    if para1 != 0:
        index = para2
    else:
        index = index + 3
    return index

def jumpIfFalse(code, index, para1, mode1, para2, mode2, relaIndex):
    if mode1 == 0:
        para1 = code[para1]
    elif mode1 == 2:
        para1 = code[para1 + relaIndex]
    if mode2 == 0:
        para2 = code[para2]
    elif mode2 == 2:
        para2 = code[para2 + relaIndex]
    if para1 == 0:
        index = para2
    else:
        index = index + 3
    return index

def lessThan(code, para1, mode1, para2, mode2, para3, mode3, relaIndex):
    if mode1 == 0:
        para1 = code[para1]
    elif mode1 == 2:
        para1 = code[para1 + relaIndex]
    if mode2 == 0:
        para2 = code[para2]
    elif mode2 == 2:
        para2 = code[para2 + relaIndex]
    if mode3 == 2:
        para3 = para3 + relaIndex
    if para1 < para2:
        code[para3] = 1
    else:
        code[para3] = 0
    
def equalTo(code, para1, mode1, para2, mode2, para3, mode3, relaIndex):
    if mode1 == 0:
        para1 = code[para1]
    elif mode1 == 2:
        para1 = code[para1 + relaIndex]
    if mode2 == 0:
        para2 = code[para2]
    elif mode2 == 2:
        para2 = code[para2 + relaIndex]
    if mode3 == 2:
        para3 = para3 + relaIndex
    if para1 == para2:
        code[para3] = 1
    else:
        code[para3] = 0

def setRelativeIndex(code, para1, mode1, relaIndex):
    if mode1 == 0:
        para1 = code[para1]
    elif mode1 == 1:
        para1 = para1
    elif mode1 == 2:
        para1 = code[relaIndex + para1]
    relaIndex += para1
    return relaIndex

def extendArray(array):
    while len(array) < 5000000:
        array.append(0)
    return array

def runIntCode(program):
    program = extendArray(program)
    index = 0
    relativeindex = 0

    while True:
        instruction = program[index]
        opcode = instruction % 100

        if( len(str(instruction)) < (opcodesSet[opcode]+2) ):
            instruction = (((opcodesSet[opcode]+2) - len(str(instruction))) * "0") + str(instruction)
            
        instruction = list(str(instruction))[:-2]
        instruction = instruction[::-1]
        instruction = [int(i) for i in instruction]

        if(opcode == 1):
            add(program, program[index+1], instruction[0], program[index+2], instruction[1], program[index+3], instruction[2], relativeindex)
            index = index + 4
        elif(opcode == 2):
            multiply(program, program[index+1], instruction[0], program[index+2], instruction[1], program[index+3], instruction[2], relativeindex)
            index = index + 4
        elif(opcode == 3):
            inputOp(program, program[index+1], instruction[0], relativeindex)
            index = index + 2
        elif(opcode == 4):
            outputOp(program, program[index+1], instruction[0], relativeindex)
            index = index + 2
        elif(opcode == 5):
            index = jumpIfTrue(program, index, program[index+1], instruction[0], program[index+2], instruction[1], relativeindex)
        elif(opcode == 6):
            index = jumpIfFalse(program, index, program[index+1], instruction[0], program[index+2], instruction[1], relativeindex)
        elif(opcode == 7):
            lessThan(program, program[index+1], instruction[0], program[index+2], instruction[1], program[index+3], instruction[2], relativeindex)
            index = index + 4
        elif(opcode == 8):
            equalTo(program, program[index+1], instruction[0], program[index+2], instruction[1], program[index+3], instruction[2], relativeindex)
            index = index + 4
        elif(opcode == 9):
            relativeindex = setRelativeIndex(program, program[index+1], instruction[0], relativeindex)
            index = index + 2
        elif(opcode == 99):
            print("Program Executed")
            break
        else:
            print("Error Occured - Invalid Opcode")

#opcode, no. parameters that it takes
opcodesSet = {
    1:3,
    2:3,
    3:1,
    4:1,
    5:2,
    6:2,
    7:3,
    8:3,
    9:1,
    99:0
}

intCode = []

with open("input.txt") as txtFile:
    line = txtFile.read()
    intCode = line.strip("\n").split(",")

for i in range(0, len(intCode)):
    intCode[i] = int(intCode[i])

runIntCode(intCode)


