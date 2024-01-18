FLOAT_CHARS = ".,"

def convertStrToInt(stringNum):
    # invalid case:
    if FLOAT_CHARS in stringNum:
        return 
    
    # getting rid of the dash so we can loop throug the integer part of the string, but making sure to remember at the end if
    # the number was negative or not, so we can return the correct result in its integer format:
    isNegative = False
    if (stringNum[0] == '-'):
        isNegative = True
        stringNum = stringNum[1:]
    
    # building up the integer format in the result variable by going thrugh each index of the string and converting the string into
    # the unicode/symbol it is representing by taking 48 - the value of ord('0'):
    result = 0
    for i in range(len(stringNum)):
        result = (result * 10) + (ord(stringNum[i]) - 48)

    # checking if the number was negative before finalising the conversion, to turn it or not into a negative value:
    if (isNegative == True):
        return -1 * result
    else:
        return result
      
for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i