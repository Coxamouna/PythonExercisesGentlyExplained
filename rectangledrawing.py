def drawRectangle(width, height):
    # invalid values check:
    if (width < 1 or height < 1):
        return 'invalid values'
    
    # print an '#' at every index within the ranges and a newline at
    # the end of the row:
    for row in range(0, height):
        for column in range(0, width):
            print('#', end='')
        print()

drawRectangle(10, 4)