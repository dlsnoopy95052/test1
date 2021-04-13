a = list(input())
b = list(input())

d = max(len(a), len(b))

aa = [0] * (d)
bb = [0] * (d)

ss = [0] * (d+1)

for i in range(len(a)):
    aa[i] = (int(a[-(i+1)]))
for i in range(len(b)):
    bb[i] = (int(b[-(i+1)]))

for i in range(d):
    ss[i] = (aa[i] + bb[i])

for i in range(d):
    j = ss[i]//10
    k = ss[i]%10
    ss[i] = k
    ss[i+1] += j

s = list(map(str, ss[::-1]))
if s[0] == '0':
    s.pop(0)

print(''.join(s))


