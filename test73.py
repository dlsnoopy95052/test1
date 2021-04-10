cube = lambda x: x ** 3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    f = []
    k = [0,1]
    for i in range(n):
        if i >= 2:
            f.append((f[i-1]+f[i-2]))
        else:
            f.append(k[i])
    return f

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))