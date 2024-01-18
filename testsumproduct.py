import random, sumproduct
numbers = []
for i in range(10000):
    numbers.append(random.randint(1, 1000000000))
print('Numbers:', numbers)
print(' Sum is', sumproduct.calculateSum(numbers))
print('Product is', sumproduct.calculateProduct(numbers))