import string
c = list(string.ascii_lowercase)

num = int(input())

r = c[0:num]
n = (num*2-1)
m = (num*2-1)*2-1

print(r,n,m)

for i in range(n):
    row = ""
    po = 0
    if i <= n//2:
        k = i
        for j in range(((m-((k*2)*2+1)))//2):
            row = row + '-'
        for p in range(2*k+1):
            if p != 0:
                row = row +'-'

            if p > (2*k+1)//2: 
                o = po +1
                po = o
            else:
                o = num -p -1
                po = o
            row = row + r[o]
            #print(row)
        for j in range(((m-((k*2)*2+1)))//2):
            row = row + '-'
        
    else:
        k = n - i -1
        for j in range(((m-((k*2)*2+1)))//2):
            row = row + '-'     
        for p in range(2*k+1):
            if p != 0:
                row = row +'-'
 
            if p > (2*k+1)//2: 
                o = po +1
                po = o
            else:
                o = num -p -1
                po = o

            row = row + r[o]

        for j in range(((m-((k*2)*2+1)))//2):
            row = row + '-'  

    print(row)