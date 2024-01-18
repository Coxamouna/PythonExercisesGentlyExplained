# ord(' ') -> 32
# chr(32) ->  ' '

# 
def printASCIITable():
    for i in range(32, 127):
        print(i, chr(i))

printASCIITable()