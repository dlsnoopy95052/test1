
N = int(input())
whole_list = []
for _ in range(N):
    arg = input().split()
    cmd = arg[0]
    if len(arg) == 2:
        value1 = int(arg[1])
    if len(arg) == 3:
        value1 = int(arg[1])
        value2 = int(arg[2])
    
    if cmd == "insert":
        whole_list.insert(value1, value2)
    if cmd == "print":
        print(whole_list)
    if cmd == "remove":
        whole_list.remove(value1)
    if cmd == "append":
        whole_list.append(value1)
    if cmd == "sort":
        whole_list.sort()
    if cmd == "pop":
        whole_list.pop()
    if cmd == "reverse":
        whole_list.reverse()
    

    
    