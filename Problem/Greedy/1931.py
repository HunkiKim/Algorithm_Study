from operator import itemgetter

N = int(input())
L = list()
for i in range(N):
    a, b = map(int, input().split())
    tu = (a, b)
    L.append(tu)
L.sort(key=itemgetter(1, 0))
e = L[0][1]
cnt = 1
for i in range(1, len(L)):
    if L[i][0] >= e:
        cnt += 1
        e = L[i][1]
print(cnt)