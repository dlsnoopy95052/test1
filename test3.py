def swap_case(s):
    orig_string_list = list(s)
    
    new_string_list = []
    for i in orig_string_list:
        if i.islower():
            new_string_list.append(i.upper())
        else:
            new_string_list.append(i.lower())
    
    return "".join(new_string_list)





s = input()
result = swap_case(s)
print(result)