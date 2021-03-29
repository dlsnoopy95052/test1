def solve(s):
    is_empty = True
    upper_name = ""
    for i in range(len(s)):
        if s[i] == " ":
            upper_name = upper_name + s[i]
            is_empty = True
        else:
            if is_empty == True:
                upper_name = upper_name + s[i].upper()
                is_empty = False
            else:
                upper_name = upper_name + s[i]

        
    return (upper_name)

    


s = input()
result = solve(s)

print(result)