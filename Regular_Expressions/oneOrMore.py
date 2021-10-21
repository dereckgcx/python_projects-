#the "+will match one or more 

import re

batRegex = re.compile(r'Bat(wo)+man') #this means such group in paranthesis must appear at least once, for instance Batman will not have any matches. 
mo1 = batRegex.search('The Adventures of Batwoman')
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo3 = batRegex.search('The Adventures of Batman')

print (f'{mo1.group()}\n {mo2.group()} \n {mo3 == None}')
