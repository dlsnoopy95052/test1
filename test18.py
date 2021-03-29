from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

product = product(a,b)

output = ""
for i in list(product):
    output += str(i)
print(output)