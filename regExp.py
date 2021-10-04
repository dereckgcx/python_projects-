def isPhoneNumber(text):
    if len(text) != 9: 
        return False
    for i in range (0, 4):
        if not text[i].isdecimal():
            return False
    if text[5] != '-':
        return False
    for i in range (6, 9):
        if not text[i].isdecimal():
            return False
    return True

print('5970-9269 is it a number?')

print (isPhoneNumber('59709269'))
