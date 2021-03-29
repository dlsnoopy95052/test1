n, m = map(int, input().split())
rows = [""] * n
message = "WELCOME"

for i in range(0,n):

    for j in range(0,m):
        k = 0

        if i == n//2:
            r = len(message)
            rows[i] = ('-' * ((m - r)//2)) + message + ('-' * ((m-r)//2))
        else: 
            k = ((n//2 - abs(n//2 - i)) * 2) + 1
            rows[i] = ('-' * ((m-3*k)//2)) + (".|." * k) + ('-' * ((m-3*k)//2))
      
    print(rows[i])

