def isPhoneNumber(text):
    if len(text)!= 9:
        return False
    for i in range (0, 4):
        if not text[i].isdecimal():
            return False
    if text[4] != '-':
        return False
    for i in range (5, 8):
        if not text[i].isdecimal():
            return False
    return True

print (isPhoneNumber('4758-0593'))
#512-512-1252
#5970-9269