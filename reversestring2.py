def reverseString(text):
    text = list(text)
    # loop over the first half of the indexes in the list:
    for i in range(len(text) // 2):
        # swap the values of i and its mirror index in the second
        # half of the list:
        mirrorIndex = len(text) - i - 1
        text[i], text[mirrorIndex] = text[mirrorIndex], text[i]
        
    return ''.join(text)

assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'
        