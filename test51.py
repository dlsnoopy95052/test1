from itertools import combinations
input()
n = list(input().split())
i = int(input())
c = 0
t = list(combinations(n, i))
for k in t:
    if 'a' in k:
        c += 1

print(round(c/len(t), 3))

