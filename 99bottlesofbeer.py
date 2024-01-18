chorus = "Take one down,\nPass it around,"
for i in range(99, -1, -1):
    if (i == 0):
        print("No more bottles of beer on the wall!\n")
    elif (i == 1):
        print(f"{i} bottle of beer on the wall,\n{i} bottle of beer,\n{chorus}\n")
    else:
        print(f"{i} bottles of beer on the wall,\n{i} bottles of beer,\n{chorus}\n")

