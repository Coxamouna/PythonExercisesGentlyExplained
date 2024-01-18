import random

def shuffle(values):
    randomIndex = random.randint(0,9)
    for i in range(0, len(values)):
        if values[i] != values[randomIndex]:
            values[i], values[randomIndex] = values[randomIndex], values[i]
            randomIndex = random.randint(0,9)
        else:
            # what are the odds?!
            randomIndex = random.randint(0,9)
            values[i], values[randomIndex] = values[randomIndex], values[i]

random.seed(42)
# Perform this test ten times:
for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)
    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10
    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Make sure an empty list shuffled remains empty:
testData2 = []
shuffle(testData2)
assert testData2 == []