import numpy

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_array = numpy.array(a)
b_array = numpy.array(b)

print(numpy.inner(a_array, b_array))
print(numpy.outer(a_array, b_array))