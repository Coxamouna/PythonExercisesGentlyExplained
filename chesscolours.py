def getChessSquareColor(column, row):
    if (column < 0 or column >= 8 or row < 0 or row >= 8):
        return ''
    if (column % 2 == row % 2):
        return 'white'
    elif (column % 2 != row % 2):
        return 'black'
 

print(getChessSquareColor(2, 4))
assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(7, 7) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''