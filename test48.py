nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []
sorted_arr = ["" for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())
# print("orignal list: ",arr)
# print("orignal sorted list:", sorted_arr)
# print("key is row ", k)
key_list = [j[k] for j in arr]
# print("key list before sorting ", key_list)
key_list = sorted(key_list)
# print("key list after sorting ", key_list)
key_value_list = {}
for p in range(n):
    key_value_list[key_list[p]] = p
#print("key/value ", key_value_list)

for q in range(n):
    sorted_arr[key_value_list[arr[q][k]]] = arr[q]

#print("sorted list ", sorted_arr)
for w in range(n):
    #print(sorted_arr[w])
    #print(type(sorted_arr[w]))
    l = ' '.join(list(map(str, sorted_arr[w])))
    print(l)


