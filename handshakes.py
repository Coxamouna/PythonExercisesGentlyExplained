def printHandshakes(people):
    # total number of handshakes:
    numberOfHandshakes = 0
    # loop over every index in the people list, except for the last one:
    for i in range(len(people) - 1):
        # loop over every index in the people list, after index i:
        for j in range(i + 1, len(people)):  
            print(f"{people[i]} shakes hands with {people[j]}")
            numberOfHandshakes += 1
    return numberOfHandshakes

assert printHandshakes(['Alice', 'Bob']) == 1
# assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
# assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6