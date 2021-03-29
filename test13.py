def solve(s):
    orig_name = list(s.split())
    upper_name = []
    for i in orig_name:
        upper_name.append(i[0].upper()+i[1:])

    return (" ".join(upper_name))

    


s = input()
result = solve(s)

print(result)