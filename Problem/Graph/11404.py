N = int(input())
M = int(input())
L = [[10000000000 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    A,B,W = map(int,input().split())
    if L[A][B]>W:
        L[A][B] = W
# print(L)
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if L[j][k] > L[j][i] + L[i][k]:
                L[j][k] = L[j][i] + L[i][k]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            print(0,end = " ")
        elif L[i][j]==10000000000:
            print(0,end=" ")
        else:
            print(L[i][j],end=" ")
    print()
