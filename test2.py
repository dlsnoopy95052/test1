from collections import Counter

num_shoes = int(input())

shoes_list = input().split()
shoes = Counter(shoes_list)

num_customers = int(input())

earned = 0

for i in range(num_customers):
    size, money = input().split()

    if size in shoes.keys():
        if shoes[size] > 0:
            shoes[size] = shoes[size] -1
            earned = earned + int(money)
        else:
            continue
    else:
        continue

print(earned)