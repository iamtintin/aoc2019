import math

def executeMove(string, wire, xpos, ypos):
    direction = string[0]
    steps = int(string[1:])
    if direction == "D":
        for i in range(0, steps):
            ypos = ypos + 1
            wire.append([xpos, ypos])
    elif direction == "U":
        for i in range(0, steps):
            ypos = ypos - 1
            wire.append([xpos, ypos])
    elif direction == "R":
        for i in range(0, steps):
            xpos = xpos + 1
            wire.append([xpos, ypos])
    elif direction == "L":
        for i in range(0, steps):
            xpos = xpos - 1
            wire.append([xpos, ypos])
    return xpos, ypos
        
with open("input.txt") as txtFile:
    lines = txtFile.readlines()

for i in range(0, len(lines)):
    lines[i] = lines[i].strip("\n").split(",")

# Starting Central Port
currentx = 10000
currenty = 10000

wire1 = []

for i in range(0, len(lines[0])):
    currentx, currenty = executeMove(lines[0][i], wire1, currentx, currenty)

currentx = 10000
currenty = 10000

wire2 = []

for i in range(0, len(lines[1])):
    currentx, currenty = executeMove(lines[1][i], wire2, currentx, currenty)

intersections = []


for i in range(0, len(wire1)):
    print(i)
    if wire1[i] in wire2:
        intersections.append(wire1[i])

distances = []

for i in range(0, len(intersections)):
    xdist = abs(10000-intersections[i][0])
    ydist = abs(10000-intersections[i][1])
    totaldistance = xdist + ydist
    distances.append(totaldistance)

print(min(distances))