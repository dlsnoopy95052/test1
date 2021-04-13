import re

s = input()
k = input()
j = 0
isempty = True
#print("***")
for i in range(len(s)+1-len(k)):
    #print(s[i:i+len(k)])
 #   print("j(loop)=", j)
 #   print(s[j:])
    m = re.search(k, s[j:])
    if m:
        a = m.start()
        b = m.end()
        a += j
        b += j
        #print("a=",a+j," b=",b+j)
        # print(s[j:])
        print("({}, {})".format(a, b-1))
        isempty = False
        j = a + 1
        #print("j=",j)
        if (j+len(k)) >= len(s):
            break
    else:
        break
if isempty:
    print("(-1, -1)")


