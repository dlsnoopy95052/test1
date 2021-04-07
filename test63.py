a = set(map(int, input().split()))
n = int(input())
result = True

for i in range(n):
    s = set(map(int, input().split()))
    if s.issubset(a) and a != s:
        continue
    else:
        result = False
print(result)