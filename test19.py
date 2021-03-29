from itertools import permutations

s, k = input().split()
r = []
o = list(permutations(list(s), int(k)))
for i in range(len(o)):
    a = ""
    for j in range(len(o[i])):
        a += o[i][j]
    r.append(a)
r.sort()
for n in range(len(r)):
    print(r[n])
