'''
    Formula - straightforward - method for the Buy 8 Get 1 Free
'''
def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    # Eg.:
    # numberOfCoffees <- 10;
    # pricePerCoffee <- 2.5;
    
    # calculate the number of free coffees we get in this order:
    numberOfFreeCoffees = numberOfCoffees // 9 # floor division
    # number of free coffees = 10 // 9 -> 1
    
    # calculate the number of coffees we will have to pay for in this order:
    numberOfPaidCoffees = numberOfCoffees - numberOfFreeCoffees
    # number of paid coffees = 10 - 1 -> 9
    
    # calculate and return the price:
    return numberOfPaidCoffees * pricePerCoffee
    # total price for 10 coffees: 9 * 2.5 -> 20
    
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