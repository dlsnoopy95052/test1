n, x = list(map(int, input().split()))
s = []
for i in range(x):
    s.append(list(map(float, input().split())))

a = list(zip(*s))
for j in range(n):
    t = 0
    for k in range(len(a[j])):
        t += a[j][k]
    print(round(t/x, 1))
