import matplotlib.pyplot as plt

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

finalImage = []

for x in range(0, height):
    finalWidth = []
    for y in range(0, width):
        finalPixel = -1
        for p in range(0, numlayers):
            if layers[p][x][y] != 2:
                finalPixel = layers[p][x][y]
                break
        finalWidth.append(finalPixel)
    finalImage.append(finalWidth)

plt.imshow(finalImage, "gray")
plt.show()