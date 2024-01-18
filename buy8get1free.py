def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    # formula attempt: 
    # total = (numberOfCoffees % 9 + int(numberOfCoffees / 9) * numberOfCoffees) * pricePerCoffee
    
    # tracking the total price
    total = 0
    
    # tracking how many coffees we have till we get a free one:
    cupsUntilFreeCoffee = 8
    
    # loop until the number of coffees is to buy reaches 0:
    while (numberOfCoffees > 0):
        # decrement the number of coffees left to buy:
        numberOfCoffees -= 1
        
        # if this cup of coffee is free, reset the number to buy
        # until a free cup back to 8:
        if (cupsUntilFreeCoffee == 0):
            cupsUntilFreeCoffee = 8
        # otherwise, pay for a cup of coffee:
        else:
            # increment the total price:
            total += pricePerCoffee
            # decrement the coffees left until we get a free coffee:
            cupsUntilFreeCoffee -= 1
    
    # return the total price:
    return total 
 
assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50
for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i
    
#  1     2     3     4    5       6      7      8    9(0)    1     2   3   4   5   6   7   8   0
# 2.5   5.0   7.5  10.0  12.5   15.0   17.5   20.0   20.0   22.5