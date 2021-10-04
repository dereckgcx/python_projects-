import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('Is the number (502) 5980-8265 ?')
print(mo.group(0))

areaCode, mainNum = mo.groups()

print (f'Area Code: {areaCode}')
print (f'Number: {mainNum}')