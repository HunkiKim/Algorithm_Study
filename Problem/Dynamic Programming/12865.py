N, K =map(int,input().split())
L = [[0 for _ in range(K+1)] for _ in range(N+1)]
T = [[0,0]]
for i in range(N):
    W,V = map(int,input().split())
    T.append([W,V])
for i in range(1,len(T)):
    v = T[i][1]
    w = T[i][0]
    # print('s')
    for j in range(K+1):
        if j<w:
            L[i][j] = L[i-1][j]
        else:
            L[i][j] = max(L[i-1][j-w]+v,L[i-1][j])

# print(L)
print(L[N][K])
