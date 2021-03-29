import cmath
a = b =''
s = input()

x = s.find('-')

if x == -1:

    a, b = s.split('+')
else:
    if s.count('-') == 1:
        if s[0] != '-':
            a, b = s.split('-')
            b = '-'+b
        else:
            a, b = s.split('+')
    else:
        a, b = s[1:].split('-')
        a = '-'+a
        b = '-'+b

b = b.replace('j','')


x = float(a)
y = float(b)

r, phi = cmath.polar(complex(x, y))
print(r)
print(phi)