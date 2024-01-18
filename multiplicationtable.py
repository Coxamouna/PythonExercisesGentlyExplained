# printing the heading of each column:
print('  | 1  2  3  4  5  6  7  8  9  10')
print('--+------------------------------')

# loop through all the numbers from 1 to 10:
for column in range(1, 11):
    # print the number label on the right side:
    print(str(column).rjust(2) + '|', end='')
    
    # loop over all the numbers from 1 to 10:
    for row in range(1, 11):
        # print the product, padded to 2 digits, followed by a space:
        print(str(column * row).rjust(2) + ' ', end='')
        
    # after the loop, print a newline to end the row:
    print()