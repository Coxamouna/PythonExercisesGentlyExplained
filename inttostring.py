# replicates the str() function:
def convertIntToStr(integerNum):
    # invalid case:
    if (integerNum != int(integerNum)):
        return 
    
    copy = abs(integerNum)
    result = ''
    
    # special case for 0 - if not added, the program fails the convertIntToStr(0) -> '0' test
    # chr(digit + 48) -> 'digit':
    while (copy > 0 or integerNum == 0):
        result += chr(copy % 10 + 48)
        copy //= 10
    
    if (integerNum >= 0):
        return result[::-1]
    else:
        return '-' + result[::-1]

# testing:    
# for i in range(-10000, 10000):
#     assert convertIntToStr(i) == str(i)
    