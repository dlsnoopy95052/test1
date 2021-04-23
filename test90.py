import numpy

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
my_array = numpy.array(a)

print(numpy.prod(numpy.sum(my_array, axis=0)))

