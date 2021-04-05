from itertools import product
def calu(a, b):
    g = 0

    for j in range(len(a)):
        q = 0
        for k in range(len(a[j])):

            q += a[j][k] ** 2
        if (q%b) > g: g= q%b
    return g


v = []
k, m = list(map(int, input().split()))
for i in range(k):
    p = list(map(int, input().split()))
    v.append(p[1:])

w = product(*v)
print(calu(list(w), m))

