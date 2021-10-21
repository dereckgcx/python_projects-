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