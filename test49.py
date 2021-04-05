nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []
sorted_arr = [] 

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

key_list = [j[k] for j in arr]

key_list = sorted(key_list)

key_value_list = {}
for p in range(n):
    key_value_list[p] = key_list[p]

for q in range(n):
    for t in range(n):
        if arr[t][k] == key_value_list[q]:
            sorted_arr.append(arr[t])
            arr.remove(arr[t])
            break
        

for w in range(n):
    l = ' '.join(list(map(str, sorted_arr[w])))
    print(l)


