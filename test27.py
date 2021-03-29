from collections import OrderedDict

items = OrderedDict()
n = int(input())
for i in range(n):
    item = input().split()
    price = int(item[-1])
    name = ' '.join(item[0:-1])

    if name in items:
        items[name] = items[name] + price
    else:
        items[name] = price


for j in items:
    print('{} {}'.format(j,items[j]))


