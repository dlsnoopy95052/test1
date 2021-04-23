import numpy

n, m, p = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
n_array = numpy.array(a)
for i in range(m):
    b.append(list(map(int, input().split())))
m_array = numpy.array(b)

print(numpy.concatenate((n_array, m_array), axis=0))
