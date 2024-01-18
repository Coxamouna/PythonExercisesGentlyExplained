def drawBorder(width, height):
    # invalid values check:
    if width < 2 or height < 2:
        return 'invalid values'
    
    # print top row:
    print('+'+('-' * (width - 2)) + '+')
    
    # loop for each row (except the top and bottom):
    for row in range(0, height - 2):
        # print the sides:
        print('|' + (' ' * (width - 2)) + '|')
    
    # print bottom row:
    print('+'+('-' * (width - 2)) + '+')
    
drawBorder(16, 4)
    