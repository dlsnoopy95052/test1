n = int(input())

s = lambda x: x ** 3

f = [0, 1]
fs = []

for i in range(n):
    #print(i)
    if i >= 2:
        f.append((f[i-1]+f[i-2]))
    #print("fs: ",fs)
    fs.append(s(f[i]))

print(fs)
        