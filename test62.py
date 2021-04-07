t = int(input())
o = []
for i in range(t):
    input()
    a = set(map(int, input().split()))
    input()
    b = set(map(int, input().split()))

    o.append(a.issubset(b))

for k in o:
    print(k)
    