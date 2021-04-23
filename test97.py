import numpy

numpy.set_printoptions(legacy='1.13')
a = list(map(float, input().split()))
a_array = numpy.array(a)

print(numpy.floor(a_array))
print(numpy.ceil(a_array))
print(numpy.rint(a_array))
