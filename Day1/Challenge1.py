import math
with open("input.txt") as txtFile:
    modules = txtFile.readlines()

total = 0

for i in range(0, len(modules)):
    modules[i] = int(modules[i].strip("\n"))
    fuel = math.floor(modules[i]/3) - 2
    modules[i] = fuel
    total += fuel

print(total)