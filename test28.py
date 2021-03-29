from collections import OrderedDict

words = OrderedDict()
n = int(input())
for i in range(n):
    word = input()
    
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1

print(len(words))

v = ""
for k in words:
    if v == "":
        v = str(words[k])
    else:
        v = v + " " + str(words[k])

print(v)
    

