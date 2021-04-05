import numpy

s = list(map(int, input().split()))

my_array = numpy.array(s)
print(numpy.reshape(my_array, (3,3)))