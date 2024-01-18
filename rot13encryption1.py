def rot13(text):
    cipher = ''
    for character in text:
        if 'a' <= character <= 'z':
            # Handle lowercase letters
            new_char = chr(((ord(character) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= character <= 'Z':
            # Handle uppercase letters
            new_char = chr(((ord(character) - ord('A') + 13) % 26) + ord('A'))
        else:
            # Keep non-alphabet characters as is
            new_char = character
        cipher += new_char
    return cipher

# testing:
assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'