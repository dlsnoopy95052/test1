import re

s = input()

match = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})[qwrtypsdfghjklzxcvbnm]', s)

if match:
    for i in match:
        print(i)
else:
    print(-1)
