def countOrbitals(orbits, index, orbitalCounter):
    planet = orbits[index][1]
    sun = orbits[index][0]
    total = 1
    if sun in orbitalCounter:
        total += orbitalCounter[sun]
    else:
        sunOrbit = findIfItOrbitsSomething(orbits, sun)
        if sunOrbit != -1:
            orbitalCounter[sun] = countOrbitals(orbits, sunOrbit, orbitalCounter)    
        else:
            orbitalCounter[sun] = 0
        total += orbitalCounter[sun]
    return total

def findIfItOrbitsSomething(orbits, key):
    found = -1
    for i in range(0, len(orbits)):
        if orbits[i][1] == key:
            found = i
    return found

with open("input.txt") as txtFile:
    lines = txtFile.readlines()

for x in range(0, len(lines)):
    lines[x] = lines[x].strip("\n").split(")")

orbitCounter = {}
total = 0

for i in range(0, len(lines)):
    total += countOrbitals(lines, i, orbitCounter)

print(total)