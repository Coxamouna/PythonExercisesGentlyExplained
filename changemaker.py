def makeChange(amount):
    # special case - amount is 0:
    if amount == 0:
        return 
    
    change = {}
    
    while amount > 0:
        if (amount // 25 > 0):
            quarters = amount // 25
            amount -= 25 * quarters
            change['quarters'] = quarters
        if (amount // 10 > 0):
            dimes = amount // 10
            amount -= 10 * dimes
            change['dimes'] = dimes
        if (amount // 5 > 0):
            nickels = amount // 5
            amount -= 5 * nickels
            change['nickels'] = nickels
        if (amount // 1 > 0):
            pennies = amount // 1
            amount -= 1 * pennies
            change['pennies'] = pennies
    
    return change
                        
assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}