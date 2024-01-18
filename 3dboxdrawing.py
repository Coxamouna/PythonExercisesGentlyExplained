def drawBox(size):
    # invalid case:
    if (size < 1):
        return
    
    # draw the back line on the top surface:
    print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')
    
    # draw top surface:
    for i in range(size):
        print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')
    
    # draw top line on top surface:
    print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')
    
    # draw front surface:
    for i in range(size - 1, -1, -1):
        print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')
        
    # draw bottom line on front surface:
    print('+' + '-' * (size * 2) + '+')
    

# box sizes from 1 to 5:
for i in range(1, 6):
    drawBox(i)
    print(f"Size {i+1}\n")