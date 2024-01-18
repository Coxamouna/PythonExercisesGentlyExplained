def getSmallest(numbers):
    if (len(numbers) == 0):
        return None
    mini = numbers[0]
    for number in numbers:
        if (mini > number):
            mini = number
    return mini

def getBiggest(numbers):
    if (len(numbers) == 0):
        return None
    maxi = numbers[0]
    for number in numbers:
        if (maxi < number):
            maxi = number
    return maxi

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None
assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3
assert getBiggest([28, 25, 42, 2, 28]) == 42
assert getBiggest([1]) == 1
assert getBiggest([]) == None