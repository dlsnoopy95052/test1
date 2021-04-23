import numpy

n, m = list(map(int, input().split()))

a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))   

a_array = numpy.array(a)
b_array = numpy.array(b)

print(a_array + b_array)
print(a_array - b_array)
print(a_array * b_array)
print(a_array // b_array)
print(a_array % b_array)
print(a_array ** b_array)

