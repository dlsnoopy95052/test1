import re
t = int(input())
u = []
r = []

def check_valid(uid):
    if re.search(r'.*[A-Z].*[A-Z].*',uid) and \
        re.search(r'.*\d.*\d.*\d.*',uid) and \
        re.search(r'[a-zA-Z0-9]{10}',uid) and\
        len(uid) == len(set(uid)):
        return "Valid"
    else:
        return "Invalid"

for i in range(t):
    u = input()
    r.append(check_valid(u))

print('\n'.join(r))