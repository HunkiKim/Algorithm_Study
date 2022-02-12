from collections import defaultdict
import string
N = input()
D = defaultdict(int)
for i in N:
    tmp = i.upper()
    D[tmp] += 1
ans = 0
realans = ''
flag = True
# print(D)
for i in D:
    if D[i] > ans:
        ans = D[i]
        realans = i
        flag = True
    elif D[i] == ans:
        flag = False
if flag==True:
    print(realans)
else:
    print('?')
