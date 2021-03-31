from itertools import combinations, combinations_with_replacement

string, num = input().split()
string = sorted(string)

l = list(combinations_with_replacement(string, int(num)))

for j in l:
    print(''.join(j))