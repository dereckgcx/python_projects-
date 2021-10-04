import re

phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d\d')

matchOb = phoneNumRegex.search('Is the number 4255-2525?')
print (f'Phone number found: {matchOb.group()}')