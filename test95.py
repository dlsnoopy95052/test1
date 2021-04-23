import numpy

n, m = list(map(int, input().split()))
c = []
for i in range(n):
    a = list(map(int, input().split()))
    c.append(a)

my_array = numpy.array(c)
print(numpy.transpose(my_array))
print(my_array.flatten())