from collections import Counter
k = int(input())

room_list = list(map(int, input().split()))

c = Counter(room_list).items()
for i in c:
    if i[1] == 1:
        print(i[0])

