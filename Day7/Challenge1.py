from itertools import permutations

def add(code, para1, mode1, para2, mode2, para3, mode3):
    if mode1 == 0:
        para1 = code[para1]
    if mode2 == 0:
        para2 = code[para2]
    code[para3] = int(para1) + int(para2)

def multiply(code, para1, mode1, para2, mode2, para3, mode3):
    if mode1 == 0:
        para1 = code[para1]
    if mode2 == 0:
        para2 = code[para2]
    code[para3] = int(para1) * int(para2)

def inputOp(code, para1, mode1, inputGiven):
    #code[para1] = input("Enter Input:")
    code[para1] = inputGiven
    
def outputOp(code, para1, mode1):
    if mode1 == 0:
        para1 = code[para1]
    print(para1)
    return para1

def jumpIfTrue(code, index, para1, mode1, para2, mode2):
    if mode1 == 0:
        para1 = code[para1]
    if mode2 == 0:
        para2 = code[para2]
    if para1 != 0:
        index = para2
    else:
        index = index + 3
    return index

def jumpIfFalse(code, index, para1, mode1, para2, mode2):
    if mode1 == 0:
        para1 = code[para1]
    if mode2 == 0:
        para2 = code[para2]
    if para1 == 0:
        index = para2
    else:
        index = index + 3
    return index

def lessThan(code, para1, mode1, para2, mode2, para3, mode3):
    if mode1 == 0:
        para1 = code[para1]
    if mode2 == 0:
        para2 = code[para2]
    if para1 < para2:
        code[para3] = 1
    else:
        code[para3] = 0
    
def equalTo(code, para1, mode1, para2, mode2, para3, mode3):
    if mode1 == 0:
        para1 = code[para1]
    if mode2 == 0:
        para2 = code[para2]
    if para1 == para2:
        code[para3] = 1
    else:
        code[para3] = 0

def runIntCode(program, input1, input2):
    index = 0
    inputIndex = 0
    output = 0

    while True:
        instruction = program[index]
        opcode = instruction % 100

        if( len(str(instruction)) < (opcodesSet[opcode]+2) ):
            instruction = (((opcodesSet[opcode]+2) - len(str(instruction))) * "0") + str(instruction)
            
        instruction = list(str(instruction))[:-2]
        instruction = instruction[::-1]
        instruction = [int(i) for i in instruction]

        if(opcode == 1):
            add(program, program[index+1], instruction[0], program[index+2], instruction[1], program[index+3], instruction[2])
            index = index + 4
        elif(opcode == 2):
            multiply(program, program[index+1], instruction[0], program[index+2], instruction[1], program[index+3], instruction[2])
            index = index + 4
        elif(opcode == 3):
            if inputIndex == 0:
                inputVar = input1
            else:
                inputVar = input2
            inputIndex += 1
            inputOp(program, program[index+1], instruction[0], inputVar)
            index = index + 2
        elif(opcode == 4):
            output = outputOp(program, program[index+1], instruction[0])
            index = index + 2
        elif(opcode == 5):
            index = jumpIfTrue(program, index, program[index+1], instruction[0], program[index+2], instruction[1])
        elif(opcode == 6):
            index = jumpIfFalse(program, index, program[index+1], instruction[0], program[index+2], instruction[1])
        elif(opcode == 7):
            lessThan(program, program[index+1], instruction[0], program[index+2], instruction[1], program[index+3], instruction[2])
            index = index + 4
        elif(opcode == 8):
            equalTo(program, program[index+1], instruction[0], program[index+2], instruction[1], program[index+3], instruction[2])
            index = index + 4
        elif(opcode == 99):
            print("Program Executed")
            break
        else:
            print("Error Occured - Invalid Opcode")    
    return output

def runAmpCode(code, inputs):
    val1 = runIntCode(code, inputs[0], 0)
    val2 = runIntCode(code, inputs[1], val1)
    val3 = runIntCode(code, inputs[2], val2)
    val4 = runIntCode(code, inputs[3], val3)
    val5 = runIntCode(code, inputs[4], val4)
    return val5

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
    99:0
}

intCode = []

with open("input.txt") as txtFile:
    line = txtFile.read()
    intCode = line.strip("\n").split(",")

for i in range(0, len(intCode)):
    intCode[i] = int(intCode[i])

perm = list(permutations([0, 1, 2, 3, 4]))

finalScores = []

for i in perm:
    i = list(i)
    finalScores.append(runAmpCode(intCode, i))

print("Yes")
print(max(finalScores))
    
