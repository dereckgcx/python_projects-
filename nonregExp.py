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

message = 'Call me tomorrow at 5970-9269 tomorrow, the office is 6661-6139.'

for i in range (len(message)):
    chunk = message [i:i+9]
    if isPhoneNumber(chunk):
        print(f'Phone number: {chunk}')
print ('Done')