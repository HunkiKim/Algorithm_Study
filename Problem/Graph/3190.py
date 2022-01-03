from collections import deque
N = int(input())
K = int(input())
L = [ [0 for _ in range(N)] for _ in range(N)]
# print(L)
for i in range(K):
    R,C = input().split()
    R,C = int(R), int(C)
    R,C = R-1,C-1
    L[R][C] = 1
K2 = int(input())
D = {}
for i in range(K2):
    X,C = input().split()
    X = int(X)
    D[X] = C

S = [1,0]
cnt = -1
x=-1
y=0
dq = deque()
while True:
    cnt+=1
    xt = x
    yt = y
    x += S[0]
    y += S[1]
    
        # print(S)
    if 0<=x<N and 0<=y<N:
        if (y,x) in dq:
            break
        elif L[y][x] == 1:
            dq.append((y,x))
            L[y][x] = 0
        else:
            if len(dq) != 0:
                tmp = dq.popleft()
                dq.append((y,x))
            else:
                dq.append((y,x))
    else:

        break






    if cnt in D:
        if D[cnt] == 'L':
            if S[0] == 1 and S[1] == 0:
                S[0] = 0
                S[1] = -1
            elif S[0] == -1 and S[1] == 0:
                S[0] = 0
                S[1] = 1
            elif S[0] == 0 and S[1] == -1:
                S[0] = -1
                S[1] = 0
            elif S[0] == 0 and S[1] == 1:
                S[0] = 1
                S[1] = 0
        elif D[cnt] == 'D':
            if S[0] == 1 and S[1] == 0:
                S[0] = 0
                S[1] = 1
            elif S[0] == -1 and S[1] == 0:
                S[0] = 0
                S[1] = -1
            elif S[0] == 0 and S[1] == -1:
                S[0] = 1
                S[1] = 0
            elif S[0] == 0 and S[1] == 1:
                S[0] = -1
                S[1] = 0    
print(cnt)