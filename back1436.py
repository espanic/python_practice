N = input()
l = len(N)
n = int(N)

import re

p = re.compile('666')

num = []

demise = []
x = 666
while len(demise) < n:
    for can in num:
        if p.search(str(can)):
            demise.append(can)
    num=list(range(x,1000*l))
    x = 1000*l
    l+=1
print(demise[n-1])

#github 수정 1번
    