import re
n = int(input())
c = []

def get_color(string):
    m = re.findall(r'\#[0-9a-f]{3,6}', string, re.IGNORECASE)
    return m

for i in range(n):
    s = input()
    if not s:
        continue
    if s[0] == '#':
        continue
    c = c + get_color(s)

print('\n'.join(c))
