n = int(input())
m = list(map(int, input().split()))
print(all(i > 0 for i in m) and any(i in [11,22,33,44,55,66,77,88,99] or i < 10 for i in m))
