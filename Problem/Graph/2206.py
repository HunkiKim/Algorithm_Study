from collections import deque
dq = deque()
N,M = map(int,input().split())
L = [list(input()) for _ in range(N)]
V = [[0 for _ in range(M)] for _ in range(N)]
V2 = [[0 for _ in range(M)] for _ in range(N)]
dq.append((0,0,1,False))
move = [(0,1),(0,-1),(-1,0),(1,0)]
V[0][0] = 1
while dq:
    # print(dq)
    y,x,cnt,flag = dq.popleft()
    if y==N-1 and x==M-1:
        print(cnt)
        exit(0)
    for i in move:
        ty = y+i[0]
        tx = x+i[1]
        if 0<=ty<N and 0<=tx<M:
            if flag==True:
                if L[ty][tx] == '0' and (V2[ty][tx]==0) :
                    V2[ty][tx] = 1
                    dq.append((ty,tx,cnt+1,flag))
            if flag == False:
                if L[ty][tx] == '0' and (V[ty][tx] == 0 or V2[ty][tx]==0) :
                    V[ty][tx] = 1
                    dq.append((ty,tx,cnt+1,flag))
                elif L[ty][tx] == '1' and flag == False and V[ty][tx] == 0 :
                    V[ty][tx] = 1
                    dq.append((ty,tx,cnt+1,True))
print(-1)
