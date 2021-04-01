from collections import deque

n = int(input())
d = deque()

for i in range(n):
    c = input().split()
    if len(c) == 2:
        a = c[0]
        b = c[1]
        if a == "append":
            d.append(b)
        elif a == "appendleft":
            d.appendleft(b)
    elif len(c) == 1:
        a = c[0]
        if a == "pop":
            d.pop()
        elif a == "popleft":
            d.popleft()
print(' '.join(d))


