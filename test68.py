import re

def check_float(string):
    if re.match('^[+|-]?\d*\.\d+$', string): # + or -, digit or none, single dot, some digits
        return True
    else:
        return False

t = int(input())
r = []
for i in range(t):
    s = input()
    r.append(check_float(s))
for j in r:
    print(j)
