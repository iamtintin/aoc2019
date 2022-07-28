total = 0
for i in range(206938, 679128):
    print("Attempting", i)
    intList = [int(x) for x in str(i)]
    if (intList == sorted(intList)):
        countInt = []
        for i in range(0, 6):
            count = intList.count(intList[i])
            countInt.append(count)
        if (2 in countInt):
            total += 1
            
print("Total:", total)