def countDigits(twoArray, key):
    count = 0
    for x in range(0, len(twoArray)):
        for y in range(0, len(twoArray[x])):
            if twoArray[x][y] == key:
                count += 1
    return count

with open("input.txt") as txtFile:
    lines = txtFile.readlines()

lines = lines[0].strip("\n")
lines = [int(x) for x in lines]

width = 25
height = 6

numlayers = int(len(lines) / (width*height))

layers = []

for l in range(0, numlayers):
    layer = []
    for h in range(0, height):
        row = []
        for w in range(0, width):
            index = (l*width*height) + (h*width) + (w)
            pixel = lines[index]
            row.append(pixel)
        layer.append(row)
    layers.append(layer)

zeroCounts = []

for i in range(0, len(layers)):
    zeroCounts.append(countDigits(layers[i], 0))

layerIndex = zeroCounts.index(min(zeroCounts))
oneCount = countDigits(layers[layerIndex], 1)
twoCount = countDigits(layers[layerIndex], 2)

print(oneCount * twoCount)
