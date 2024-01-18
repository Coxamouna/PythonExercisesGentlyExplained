def commaFormat(number):
    # convert the number to a string:
    number = str(number)
    
    # remember the fractional part and remove it from the number, if any:
    if ('.' in number):
        fractionalPart = number[number.index('.'):]
        number = number[:number.index('.')]
    else:
        fractionalPart = ''
        
    # create a variable to hold triples of digits and the comma formatted
    # tring as it is built:
    
    triplet = ''
    commaNumber = ''
    
    # loop over the digits starting on the right side and going left:
    for i in range(len(number) - 1, -1, -1):
        # add the digits to the triplet variable:
        triplet = number[i] + triplet
        # when the triplet variable has three digits, add it with a
        # comma to the comma-formatted string:
        if (len(triplet) == 3):
            commaNumber = triplet + ',' + commaNumber
            # reset the triplet variable bacl to a blank string:
            triplet = ''
    
    # if the triplet has any digits left over, add it with a comma
    # to the comma-formatted string:
    if (triplet != ''):
        commaNumber = triplet + ',' + commaNumber
        
    # return the comma-formatted string:
    return commaNumber[:-1] + fractionalPart

assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'
    