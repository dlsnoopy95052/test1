import re
n = int(input())
r = []
for i in range(n):
    if re.match(r'^[789]\d{9}$', (input())):
        r.append("YES")
    else:
        r.append("NO")

print('\n'.join(r))
