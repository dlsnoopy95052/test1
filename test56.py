import numpy

n = int(input())
a = []
b = []
for i in range(n):
    a.append(list(map(float, input().split())))

print(round(numpy.linalg.det(a), 2))

