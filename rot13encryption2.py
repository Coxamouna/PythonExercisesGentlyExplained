def rot13(text):
    encryptedText = ''
    for character in text:
        if not character.isalpha():
            encryptedText += character
        else:
            rotatedLetterOrdinal = ord(character) + 13
            
    # If adding 13 pushes the letter past z or Z, subtract 26:
    if character.islower() and rotatedLetterOrdinal > 122:
        rotatedLetterOrdinal -= 26
    if character.isupper() and rotatedLetterOrdinal > 90:
        rotatedLetterOrdinal -= 26
    # Add the encrypted letter to encryptedText:
    encryptedText += chr(rotatedLetterOrdinal)
    # Return the encrypted text:
    return encryptedText