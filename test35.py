m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

d = a.difference(b)
#print(d)
e = b.difference(a)
#print(e)
f = list(e.union(d))
f.sort()
for i in f:
    print(i)