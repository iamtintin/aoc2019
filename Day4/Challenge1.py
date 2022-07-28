total = 0
for i in range(206938, 679128):
    print("Attempting", i)
    intList = [int(x) for x in str(i)]
    if (intList == sorted(intList)):
        if len(intList) != len(set(intList)):
            total += 1
            
print("Total:", total)