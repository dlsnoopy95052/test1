import string
all_letters = list(string.ascii_uppercase)
consonants = []
string = "BANANA"
vowels = ['A','E','I','O','U']
for s in all_letters:
    if s not in vowels:
        consonants.append(s)
kevin_score = 0
stuart_score = 0

kevin_dict = {}
stuart_dict = {}

for i in range(len(string)): # substring len
    for j in range(len(string)-i):
        #print("checking ", string[j:j+i+1])
        if string[j] in vowels:
            kevin_score += 1
            # if string[j:j+i+1] in kevin_dict:
            #     kevin_dict[string[j:j+i+1]] +=  1
            # else:
            #     kevin_dict[string[j:j+i+1]] = 1
        else:
            stuart_score += 1
            # if string[j:j+i+1] in stuart_dict:
            #     stuart_dict[string[j:j+i+1]] += 1
            # else:
            #     stuart_dict[string[j:j+i+1]] = 1
        
if kevin_score > stuart_score:
    print("Kevin ", kevin_score)
elif stuart_score > kevin_score:
    print("Stuart ", stuart_score)
else:
    print("Draw")



