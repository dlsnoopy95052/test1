s = list(input())

low = []
upp = []
odd = []
even = []

for i in s:
    if i.islower():
        low.append(i)
    elif i.isupper():
        upp.append(i)
    else:
        if (int(i) % 2) == 0:
            even.append(i)
        else:
            odd.append(i)
print("{}{}{}{}".format(''.join(sorted(low)),''.join(sorted(upp)),''.join(sorted(odd)),''.join(sorted(even))))