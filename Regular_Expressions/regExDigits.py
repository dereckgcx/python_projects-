import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d\d-\d\d\d\d)') #will look for digits

mo = phoneNumRegex.search('Is the number (502) 5980-8265 ?')
print(mo.group(0)) #with specific index a group can be called, 0 will return the entire match

areaCode, mainNum = mo.groups() #will return a tuple of all the groups separately

print (f'Area Code: {areaCode}')
print (f'Number: {mainNum}')

#

phoneRegex = re.compile(r'(\(\d\d\d\))?\d\d\d\d-\d\d\d\d') #match zero or one of the group preceding the question mark
mox = phoneRegex.search('My current phone number is (502)5970-9268')
print (mox.group())

mox1 = phoneRegex.search('My current phone number is 4136-6940')
print (mox1.group())