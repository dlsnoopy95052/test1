import numpy
a = []
b = []

n = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))

a_array = numpy.array(a)
b_array = numpy.array(b)
print(numpy.matmul(a_array,b_array))