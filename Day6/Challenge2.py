def createOrbitList(orbits, index):
    planet = orbits[index][1]
    sun = orbits[index][0]
    orbitalList = [sun]

    sunOrbit = findIfItOrbitsSomething(orbits, sun)
    sunOrbitList = []

    if sunOrbit != -1:
        sunOrbitList = createOrbitList(orbits, sunOrbit)    
    orbitalList = orbitalList + sunOrbitList
    return orbitalList

def findIfItOrbitsSomething(orbits, key):
    found = -1
    for i in range(0, len(orbits)):
        if orbits[i][1] == key:
            found = i
    return found

def findCommonElements(list1, list2):
    for i in range(0, len(list1)):
        for x in range(0, len(list2)):
            if (list1[i] == list2[x]) and (list1[i+1] == list2[x+1]):
                return i, x

with open("input.txt") as txtFile:
    lines = txtFile.readlines()

for x in range(0, len(lines)):
    lines[x] = lines[x].strip("\n").split(")")

myIndex = findIfItOrbitsSomething(lines, "YOU")
sanIndex = findIfItOrbitsSomething(lines, "SAN")

youList = createOrbitList(lines, myIndex)
sanList = createOrbitList(lines, sanIndex)

uCommon, sCommon = findCommonElements(youList, sanList)
uCommon = len(youList) - uCommon
sCommon = len(sanList) - sCommon

youList = youList[:len(youList)-uCommon+1]
sanList = sanList[:len(sanList)-sCommon]

moves = len(youList) - 1 + len(sanList)

print(moves)