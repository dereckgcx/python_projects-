import re

phoneNumRegex = re.compile(r'(\d\d\d) (\d\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('Is the number 502 5980-8265cle?')
print(mo.group(0))
