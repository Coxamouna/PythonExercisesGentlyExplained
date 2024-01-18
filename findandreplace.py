def findAndReplace(text, oldText, newText):
    replacedText = ''
    i = 0
    while (i < len(text)):
        # if index i in text is the start of the oldText pattern,
        # add the replacement text
        if text[i:i+len(oldText)] == oldText:
            # add the replacement text:
            replacedText += newText
            # increment i by the length of the oldText:
            i += len(oldText)
        # otherwise, add the characters at text[i] and increment i by 1:
        else:
            replacedText += text[i]
            i += 1
    return replacedText

print(findAndReplace('Bitches they come and go', 'Bitches', 'Leeches'))

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'