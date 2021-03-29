s = list(input())
alphanumeric = False
alphabetical = False
digit = False
lowercase = False
uppercase = False

for c in s:
    
    if c.isalpha():
        alphabetical = True
        if c.isupper():
            uppercase = True
        else:
            lowercase = True            
    if c.isdigit():
        digit = True
if digit or alphabetical:
    alphanumeric = True

print(alphanumeric)
print(alphabetical)
print(digit)
print(lowercase)
print(uppercase)

