# the star/asterisk "*" character means match zero or more.
# the group that precedes such can occur any number of times to coincide for a match
 
import re

batRegex = re.compile(r'Bat(wo)*man')
mou1 = batRegex.search('The adventures of Batwowowowowowowowoman')
mou2 = batRegex.search('The adventures of Batwowoman')
mou3 = batRegex.search('The adventures of Batwoman')

print   (mou1.group(),'\n',
        mou2.group(),'\n',
        mou3.group())

