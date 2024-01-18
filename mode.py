import random
def mode(numbers):
    # specia case: if the number list is empty, return none:
    if (len(numbers) == 0):
        return None

    # dictionary with keys of numberss and values of how often they appear:
    numberCount = {}
    
    # track the most frequent number and how often it appers:
    mostFreqNumber = None
    mostFreqNumberCount = 0
    
    # loop through all the numbers, counting how often they apper:
    for number in numbers:
        # if the number hasn't appeared before, set it's count to 0.
        if number not in numberCount:
            numberCount[number] = 0
        # increment the number's count
        numberCount[number] += 1
        # if this is more frequent than the most frequent number,
        # it becomes the new most frequent number
        if numberCount[number] > mostFreqNumberCount:
            mostFreqNumber = number
            mostFreqNumberCount = numberCount[number]
    # the function return the most frequent number
    return mostFreqNumber

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1

random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4