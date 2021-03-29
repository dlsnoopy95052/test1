
def average(array):
    arr_set = set(array)
    v = 0
    n = 0
    for i in arr_set:
        v = v + i
        n += 1
    
    return (v/n)

    




n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)