def wrapper(f):
    def fun(l):
        # complete the function
        #print(l)
        lst = []
        for i in range(len(l)):
            num = "+91 {} {}".format(l[i][-10:-5], l[i][-5:])
            lst.append(num)
        return f(sorted(lst))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

