import math

def findFuelRequiredForModule(mass):
    totalFuel = 0
    while True:
        fuel = math.floor(mass/3) - 2
        if fuel <= 0:
            break
        totalFuel += fuel
        mass = fuel
    return totalFuel

with open("input.txt") as txtFile:
    modules = txtFile.readlines()

total = 0

for i in range(0, len(modules)):
    modules[i] = int(modules[i].strip("\n"))
    total += findFuelRequiredForModule(modules[i])
    
print(total)