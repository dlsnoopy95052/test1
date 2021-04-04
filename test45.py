t = int(input())
for _ in range(t):
    b = int(input())
    bs = list(map(int, input().split()))
    i = 0
    j = len(bs)-1
    last_value = -1
    no = False
    while i != j:

        if last_value != -1:
            if bs[i] >= bs[j] and bs[i] <= last_value:
                last_value = bs[i]
                i += 1
            elif bs[i] < bs[j] and bs[j] <= last_value:
                last_value = bs[j]
                j -= 1
            else:
                print("No")
                no = True
                break
        else:
            if bs[i] >= bs[j]:
                last_value = bs[i]
                i += 1
            elif bs[i] < bs[j]:
                last_value = bs[j]
                j -= 1
            else:
                print("No")
                no = True
                break
    if no == False: print("Yes")


