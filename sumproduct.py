def calculateSum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

def calculateProduct(numbers):
    prod = 1
    for number in numbers:
        prod *= number
    return prod 

assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
