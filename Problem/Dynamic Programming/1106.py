ans, n = map(int, input().split())
D = list(10000 for _ in range(ans * 2))
Dic = {}
for i in range(n):
    a, b = map(int, input().split())
    Dic[a] = b
c = 0
D[0] = 0
DicK = list(Dic.keys())
while True:
    if c == ans:
        break
    for i in DicK:
        if Dic[i] == c:
            D[c] = i
        else:
            D[Dic[i] + c] = min(D[Dic[i] + c], i + D[c])
    print(D[c])
    c += 1

print(D[ans])
