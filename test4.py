def mutate_string(string, position, character):
    first_part = string[0:position]
    last_part = string[position+1:]

    return (first_part+character+last_part)


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
