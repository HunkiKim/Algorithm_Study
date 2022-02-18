from collections import deque
N, M = map(int,input().split())
L = list()
for i in range(N):
    L.append(list(map(int,input().split())))
move = [(0,1),(0,-1),(1,0),(-1,0)]
anscnt = 0
while True:
    # print(L)
    
    cnt = 0
    dq = deque()
    dq.append((0,0))
    V = [[True for _ in range(M)] for _ in range(N)]
    V[0][0] = False
    while dq:
        y,x = dq.popleft()
        cnt += 1
        for i in move:
            ty = y+i[1]
            tx = x+i[0]
            if 0<=ty<N and 0<=tx<M and L[ty][tx] == 0 and V[ty][tx] == True:
                V[ty][tx] = False
                dq.append((ty,tx))
    if cnt >= N*M:
        # print(L)
        break
    anscnt+=1
    for i in range(N):
        for j in range(M):
            if L[i][j] == 1:
                c_cnt = 0
                if 0<j<M-1 and not V[i][j+1] and not V[i][j-1]:
                    L[i][j] = 0
                elif j==0 and not V[i][j+1]:
                    L[i][j] = 0
                elif j==M-1 and not V[i][j-1]:
                    L[i][j] = 0
                else:
                    for k in move:
                        ty = i+k[1]
                        tx = j+k[0]
                        if 0<=ty<N and 0<=tx<M and L[ty][tx] == 0 and V[ty][tx] == False:
                            c_cnt += 1
                    if c_cnt>=2:
                        L[i][j] = 0
print(anscnt)

    
