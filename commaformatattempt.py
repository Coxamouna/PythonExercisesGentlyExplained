# In the US and UK, the digits of numbers are grouped with commas
# every three digits. For example, the number 79033516 
# is written as 79,033,516 for:
def commaFormat(number):
    numberString = str(number)[::-1]
    result = ''
    groupSize = 0
    isDot = False
    
    for i in range(0, len(numberString)):
        # result stores every character of the reverse number string:
        result += numberString[i]
        groupSize += 1
        
        # check is the index reached the decimal point:
        if (numberString[i] == '.'):
            isDot = True
        
        # if the number is an integer, add the comma(',') after every group of
        # 3 digits and then resets the group size back to zero.
        # if the number is a floating-point number, isDot becomes True when the index reaches it
        # but also the adding of a comma after the decimal point will stop. 
        if (isDot == False):
            if (groupSize != 0):
                if(groupSize % 3 == 0 and len(numberString) > 3):
                    result += ','
                    groupSize = 0
        else:
            continue

    result = result[::-1]
    if (result[0] == ','):
        return result[1:]
    else:
        return result
            
# print(type(commaFormat(100000000000)))
# print(commaFormat(100000))
# testing:
# assert commaFormat(1) == '1'
# assert commaFormat(10) == '10'
# assert commaFormat(100) == '100'
# assert commaFormat(1000) == '1,000'
# assert commaFormat(10000) == '10,000'
# assert commaFormat(100000) == '100,000'
# assert commaFormat(1000000) == '1,000,000'
# assert commaFormat(1234567890) == '1,234,567,890'
# assert commaFormat(1000.123456) == '1,000.123456'
print(commaFormat(10000000.1234))