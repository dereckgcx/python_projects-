import re

# given a group that needs to be repeated a set number of times: braces with such number most procede the group
# (Hey){3} = (Hey)(Hey)(Hey)
# (Hey){3,5} = (Hey)(Hey)(Hey)|(Hey)(Hey)(Hey)(Hey)|(Hey)(Hey)(Hey)(Hey)(Hey)


heyRegex = re.compile(r'(hey){3}')
hey1 = heyRegex.search('heyheyhey') #this will find a match since it has 3 groups of "hey" 
hey2 = heyRegex.search('hey') #whereas this one won't since it only has one group of "hey"

print (hey1.group())
print (hey2 == None)

# GREEDY AND NON GREEDY MATCHING

