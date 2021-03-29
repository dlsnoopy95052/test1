j = int(input())

def print_formated(number):
    number_string = str(bin(number))
    width = len(number_string)-2
    #print(number_string, width)
    for i in range(number):
        v = i + 1
        o = ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(v, width=width))
        print(o)


print_formated(j)