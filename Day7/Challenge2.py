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
    #print(para1)
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

def runIntCode(program, input1, input2, startingIndex, inputIndex):
    index = startingIndex
    output = 0
    exitCode = 0

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
            #print("Input no.", inputIndex, inputVar)
            inputOp(program, program[index+1], instruction[0], inputVar)
            index = index + 2
        elif(opcode == 4):
            output = outputOp(program, program[index+1], instruction[0])
            index = index + 2
            break
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
            print("Program Executed.")
            exitCode = 1
            break
        else:
            print("Error Occured - Invalid Opcode")
        #print("Exit", exitCode)
    return output, index, program, exitCode

def runAmpCode(amp1Code, amp2Code, amp3Code, amp4Code, amp5Code, inputs, firstInput, ampStartingIndexs, loopCount):
    amp1out, ampStartingIndexs[0], amp1Code, exeCode = runIntCode(amp1Code, inputs[0], firstInput, ampStartingIndexs[0], loopCount)
    amp2out, ampStartingIndexs[1], amp2Code, exeCode = runIntCode(amp2Code, inputs[1], amp1out, ampStartingIndexs[1], loopCount)
    amp3out, ampStartingIndexs[2], amp3Code, exeCode = runIntCode(amp3Code, inputs[2], amp2out, ampStartingIndexs[2], loopCount)
    amp4out, ampStartingIndexs[3], amp4Code, exeCode = runIntCode(amp4Code, inputs[3], amp3out, ampStartingIndexs[3], loopCount)
    amp5out, ampStartingIndexs[4], amp5Code, exeCode = runIntCode(amp5Code, inputs[4], amp4out, ampStartingIndexs[4], loopCount)
    return amp5out, amp1Code, amp2Code, amp3Code, amp4Code, amp5Code, ampStartingIndexs, exeCode


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

orders = list(permutations([5, 6, 7, 8, 9]))
finalScores = []

for i in orders:
    code1 = intCode.copy()
    code2 = intCode.copy()
    code3 = intCode.copy()
    code4 = intCode.copy()
    code5 = intCode.copy()
    
    programCode = 0
    firstValue = 0
    phaseInputs = list(i)
    programIndices = [0, 0, 0, 0, 0]
    counter = 0

    while programCode != 1:
        previousFirstValue = firstValue
        firstValue, code1, code2, code3, code4, code5, programIndices, programCode = runAmpCode(code1, code2, code3, code4, code5, phaseInputs, firstValue, programIndices, counter)
        if programCode == 1:
            firstValue = previousFirstValue
        counter += 1

    finalScores.append(firstValue)

print(max(finalScores))
