import re
import itertools
n = int(input())

u = []
r = []

def check_valid(card_no):
    if re.match(r'^[456]+[0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$',card_no) or \
        re.match(r'[456]+[0-9]{15}',card_no):
        s = ''.join(filter(str.isdigit, card_no))
        for (key, group) in itertools.groupby(s):
            if len(list(group)) >= 4:
                return "Invalid"
        return "Valid"
    else:
        return "Invalid"

for i in range(n):
    u = input()
    r.append(check_valid(u))

print('\n'.join(r))