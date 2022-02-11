from collections import deque

M,N,K = map(int,input().split())
L = [[0 for _ in range(N)] for _ in range(M)]
for i in range(K):
    tmp = list(map(int,input().split()))
    for j in range(tmp[0],tmp[2]):
        for k in range(tmp[1],tmp[3]):
            L[k][j] = 1
dq = deque()
cnt = 0
move = [(1,0),(-1,0),(0,1),(0,-1)]
ans = []
# print(L)
for i in range(M):
    for j in range(N):
        if L[i][j] == 0:
            dq.append((i,j))
            L[i][j] = 1
            cnt = 0
            while dq:
                y,x = dq.popleft()
                cnt += 1
                for ii in move:
                    ty = ii[1] + y
                    tx = ii[0] + x
                    if 0<=tx<N and 0<=ty<M and L[ty][tx] == 0:
                        L[ty][tx] = 1
                        dq.append((ty,tx))

            ans.append(cnt)
ans.sort()
print(len(ans))
print(*ans)
