import random

LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz" # 26 characters
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 26 characters
NUMBERS = "1234567890" # 10 characters
SPECIAL = "~!@#$%^&*()_+" # 13 characters
ALL_CHARACTERS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL # 75 characters

def generatePassword(length):    
    # check if the lenght is less than 12; if so, set it to 12
    if (length < 12):
        length = 12

    # empty list for password variable, which will hold at least one
    # character from each of the four categories(const variables)
    password = []
    
    # add a random character from the lowercase, uppercase, numbers,
    # and special character strings:
    password.append(LOWER_LETTERS[random.randint(0,25)])
    password.append(UPPER_LETTERS[random.randint(0,25)])
    password.append(NUMBERS[random.randint(0,9)])
    password.append(SPECIAL[random.randint(0,12)])
    
    # keep adding random character from the combined string until the
    # password meets the length:
    while (len(password) < length):
        password.append(ALL_CHARACTERS[random.randint(0,74)])
        
    # randomly shuffle the password list:
    random.shuffle(password)
    
    # join all the strings in the password list onto one string to return:
    return ''.join(password)

# print(f"New password for Runescape: {generatePassword(16)}")
   
assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial