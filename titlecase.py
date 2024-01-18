from passwordgenerator import LOWER_LETTERS, UPPER_LETTERS
ALL_LETTERS = LOWER_LETTERS + UPPER_LETTERS

def getTitleCase(text):
    titledText = ''
    
    for i in range (0, len(text)):
        character = text[i]
        # if it's the first character, we up it anyway:
        if (i == 0):
            titledText += character.upper()
        # if the character before wasn't a letter, we up it:
        elif (text[i-1] not in ALL_LETTERS and character in ALL_LETTERS):
            titledText += character.upper()
        else:
            titledText += character.lower()
            
    return titledText

assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'
