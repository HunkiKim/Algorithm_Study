L = list()
cnt = 1
while len(L)<1000:
    for i in range(cnt):
        L.append(cnt)
    cnt += 1
a,b = map(int,input().split())
a,b = (a-1), (b-1)
ans = 0
for i in range(a,b+1):
    ans += L[i]
print(ans)