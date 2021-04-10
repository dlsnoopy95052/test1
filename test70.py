import itertools
import re

s = list(input())
#print(s)
r = []
for (key, group) in itertools.groupby(s):
    r.append([key, list(group)])

#print(r)
for k in range(len(r)):
    if re.match('^[a-zA-Z0-9]+$',r[k][0]):
        if len(r[k][1]) > 1:
            print(r[k][0])
            exit()
    else:
        continue
print(-1)