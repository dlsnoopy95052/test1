from itertools import combinations

string, num = input().split()
string = sorted(string)

for i in range(int(num)):
    l = list(combinations(string, i+1))

    for j in l:
        print(''.join(j))
