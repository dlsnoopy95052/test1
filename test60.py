v = input()
a = set(map(int, input().split()))
cn = int(input())
sm = 0

for _ in range(cn):
    cm, nm = (input().split())
    lm = set(map(int, input().split()))
    if cm == "intersection_update":
        a.intersection_update(lm)
    elif cm == "update":
        a.update(lm)
    elif cm == "symmetric_difference_update":
        a.symmetric_difference_update(lm)
    elif cm == "difference_update":
        a.difference_update(lm)
    else:
        print("bad operation name")
        exit()
for i in a:
    sm += i
print(sm)
