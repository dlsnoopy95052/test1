import numpy

a = tuple(map(int, input().split()))

print(numpy.zeros(a, dtype=int))
print(numpy.ones(a, dtype=int))