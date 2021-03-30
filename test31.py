n, m = list(map(int, input().split()))
arr = input().split()

a_set = set(input().split())
b_set = set(input().split())

print(len(a_set))
print(len(b_set))
happiness = 0

for i in arr:
    if i in a_set:
        happiness += 1
    if i in b_set:
        happiness -= 1


# z = a_set.intersection(arr)
# if z:
#     print(z)
#     happiness += len(z)

# v = b_set.intersection(arr)
# if v:
#     print(v)
#     happiness -= len(v)


print(happiness)