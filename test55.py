import numpy

v = list(map(float, input().split()))

print(numpy.polyval(v, int(input())))