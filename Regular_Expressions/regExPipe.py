# | is a pipe, is used to match one of many expressions, both occurences will only validate 
# the first as the Match object.
import re

heroRegex = re.compile(f'Batman|Tina Fey') 
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()

print(mo.group(1))

#optional pattern matching using "?" character

batRegex = re.compile(r'Bat(wo)?man') #this section specifies the optional part
mo3 = batRegex.search('The Adventures of Batwoman')
print (mo3.group())

#

phoneRegex = re.compile(r'(\(\d\d\d\))?\d\d\d\d-\d\d\d\d')
mox = phoneRegex.search('My current phone number is (502)5970-9268')
print (mox.group())

mox1 = phoneRegex.search('My current phone number is 4136-6940')
print (mox1.group())