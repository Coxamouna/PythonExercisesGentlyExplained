LOWER_LETTERS = {"abcdefghijklmnopqrstuvwxyz"}

def getUppercase(text):
    uppedText = ''
    for character in text:
        if character in LOWER_LETTERS:
            characterOrd = ord(character) + 32
            uppedText += chr(characterOrd)
        else:
            uppedText += character
    
    return uppedText

print(getUppercase('hello'))
# assert getUppercase('Hello') == 'HELLO'
# assert getUppercase('hello') == 'HELLO'
# assert getUppercase('HELLO') == 'HELLO'
# assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
# assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
# assert getUppercase('12345') == '12345'
# assert getUppercase('') == ''