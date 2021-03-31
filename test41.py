from itertools import groupby
groups=[]
keys=[]
output = ""
s = input()

for k, g in groupby(s):
    groups.append(list(g))
    keys.append(k)

for i in range(len(keys)):
    if output == "":
        output = '({}, {})'.format(len(groups[i]), keys[i])
    else:
        output += ' ({}, {})'.format(len(groups[i]), keys[i])

print(output)


