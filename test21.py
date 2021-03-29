import math
a = float(input())
b = float(input())

rad = math.atan2(a, b)
deg = math.degrees(rad)
print("{}\N{DEGREE SIGN}".format(round(deg)))