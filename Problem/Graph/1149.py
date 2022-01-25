N = int(input())
L = list()
for i in range(N):
    L.append(list(map(int,input().split())))
for i in range(1,N):
    L[i][0] = min(L[i-1][1],L[i-1][2]) + L[i][0]
    L[i][1] = min(L[i-1][0],L[i-1][2]) + L[i][1]
    L[i][2] = min(L[i-1][1],L[i-1][0]) + L[i][2]
ans = min(L[-1][0], L[-1][1], L[-1][2])
print(ans)
