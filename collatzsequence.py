import random

def collatz(startingNumber):
    sequence = []
    
    # special case
    if startingNumber == 0:
        return []
    
    # base case
    if startingNumber == 1:
        return sequence
    # "recursive" case
    else:
        while(startingNumber != 1):
            if startingNumber % 2 == 0:
                sequence.append(startingNumber)
                startingNumber //= 2
            else:
                sequence.append(startingNumber)
                startingNumber = 3 * startingNumber + 1
        sequence.append(startingNumber)
        return sequence

assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123

random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum # Make sure it includes the starting number.
    assert seq[-1] == 1 # Make sure the last integer is 1.