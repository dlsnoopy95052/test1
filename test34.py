n = int(input())
s = set(map(int, input().split()))
N = int(input())
total = 0
for i in range(N):

    paras = input().split()
    if paras[0] == "pop":
        s.pop()
    
    if len(paras) > 1:
        if paras[0] == "remove":
            try:
                s.remove(int(paras[1]))
            except KeyError:
                print("KeyError")
        elif paras[0] == "discard":
            s.discard(int(paras[1]))
    
for j in s:
    total += j

print(total)