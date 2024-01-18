def drawPyramid(height):
    if (height < 1):
        return
    # loop over each row from 0 up to height:
    for rowNumber in range(height):
        # create a string of spaces for the left side of the pyramid:
        leftSideSpaces = ' ' * (height - (rowNumber + 1))
        # create the string of hashtags for this row of the pyramid:
        pyramidRow = '#' * (rowNumber * 2 + 1)
        # print the left side spaces and the row of the pyramid:
        print(leftSideSpaces + pyramidRow)
        
drawPyramid(6)