intCode = []

with open("input.txt") as txtFile:
    line = txtFile.read()
    intCode = line.strip("\n").split(",")

for i in range(0, len(intCode)):
    intCode[i] = int(intCode[i])

intCode[63] = 34463338 * 34463338

if intCode[63] < 34463338:
    intCode[63] = 1
else:
    intCode[63] = 0

if intCode[63] != 0:
    print("Hello")
