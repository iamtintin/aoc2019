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

def inputOp(code, para1, mode1):
    code[para1] = input("Enter Input:")
    
def outputOp(code, para1, mode1):
    if mode1 == 0:
        para1 = code[para1]
    print(para1)

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

def runIntCode(program):
    index = 0

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
            inputOp(program, program[index+1], instruction[0])
            index = index + 2
        elif(opcode == 4):
            outputOp(program, program[index+1], instruction[0])
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

runIntCode(intCode)


