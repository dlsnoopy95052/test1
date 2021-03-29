from collections import defaultdict

a, b = map(int, input().split())
group = defaultdict(list)

for i in range(a):
    group['GROUP_A'].append(input())
for j in range(b):
    group['GROUP_B'].append(input())


for i in group['GROUP_B']:

    j = group['GROUP_A']

    string = ""
    for k in range(len(group['GROUP_A'])):

        if group['GROUP_A'][k] == i:
            if string != "":
                string = string + " " + str(k+1)
            else:
                string = str(k+1)

    if string == "":
        print("-1")
    else:
        print(string)

    
