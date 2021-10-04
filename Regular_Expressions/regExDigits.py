import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d\d-\d\d\d\d)') #will look for digits

mo = phoneNumRegex.search('Is the number (502) 5980-8265 ?')
print(mo.group(0)) #with specific index a group can be called, 0 will return the entire match

areaCode, mainNum = mo.groups() #will return a tuple of all the groups separately

print (f'Area Code: {areaCode}')
print (f'Number: {mainNum}')

