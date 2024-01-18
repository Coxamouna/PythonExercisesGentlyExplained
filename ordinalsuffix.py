def ordinalSuffix (number):
    string = str(number)
    for i in string:
        if string[-2:] in ('11', '12', '13'):
            return string + "th"
        if string[-1] == '1':
            return string + "st"
        if string[-1] == '2':
            return string + "nd"
        if string[-1] == '3':
            return string + "rd"
        return string + "th"

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'