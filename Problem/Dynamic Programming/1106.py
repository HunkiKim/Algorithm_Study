C,N = map(int,input().split())
INF = 10000000000
L = [INF for _ in range(C+1)]
D = {}
L[0] = 0
for i in range(N):
    a,b = map(int,input().split())
    D[b] = a
    L[b] = a

for i in range(C+1):
    print(L)
    for j in D:
        if i+j>=C:
            L[C] = min(L[C],L[i] + D[j])
        else:
            L[i+j] = min(L[i+j],L[i] + D[j])

print(L[-1])