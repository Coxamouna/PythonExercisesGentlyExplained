import random, average

def median(numbers):
    numbers.sort()
    if (len(numbers) == 0):
        return None
    if (len(numbers) % 2 == 1):
        number = len(numbers) / 2
        return numbers[int(number)]
    if (len(numbers) % 2 == 0):
        number1 = len(numbers) / 2
        number2 = number1 - 1
        return average.average([numbers[int(number1)], numbers[int(number2)]])        

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6