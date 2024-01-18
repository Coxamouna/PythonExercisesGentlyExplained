def fizzBuzz(upTo):
    for num in range(1, upTo+1):
        if (num % 15 == 0): 
            print("FizzBuzz", end = ' ')
        elif (num % 3 == 0):
            print("Fizz", end = ' ')
        elif (num % 5 == 0):
            print("Buzz", end = ' ')
        else:
            print(num, end =' ')


fizzBuzz(34)
#test case for fizzbuzzing