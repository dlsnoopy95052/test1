import re
c = []
i = int(input())
for j in range(i):
    x = input()
    a = re.sub(r"(?<=(\s))\|\|\s", "or ", x)
    #print(a)
    b = re.sub(r"(?<=(\s))\&\&\s", "and ", a)
    c.append(b)

print('\n'.join(c))

