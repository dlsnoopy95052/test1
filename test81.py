import re
import email.utils as utils

n = int(input())
elist = []

def verify_email(email):
    m = re.match(r'^[a-z][a-z0-9-._]+@[a-z]+\.[a-z]{1,3}$', email, re.IGNORECASE)
    if m:
        return True
    else:
        return False

for i in range(n):
    n, a = utils.parseaddr(input())

    if verify_email(a) == False:
        continue
    elist.append([n, a])

for i in elist:
    print('{} <{}>'.format(i[0], i[1]))