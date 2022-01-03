from collections import deque
N,M = map(int,input().split())
L = list()
for i in range(N):
    tmp = list(map(int,input().split()))
    L.append(tmp)

di = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
cl = list()
cl.append((N-1,0))
cl.append((N-1,1))
cl.append((N-2,0))
cl.append((N-2,1))
N2 = N-1
for i in range(M):
    s,d = map(int,input().split())
    s -= 1
    direction = di[s]   
    for k in range(d):
        for j in range(len(cl)):
            cl[j] = ((cl[j][0] + direction[0]) % N, (cl[j][1] + direction[1]) % N)
            
    for j in cl:
        L[j[0]][j[1]] += 1
    for j in range(len(cl)):
        tmp1 = (cl[j][0]-1, cl[j][1]-1)
        tmp2 = (cl[j][0]-1, cl[j][1]+1)
        tmp3 = (cl[j][0]+1, cl[j][1]+1)
        tmp4 = (cl[j][0]+1, cl[j][1]-1)
        if 0<=tmp1[0]<N and 0<=tmp1[1]<N and L[tmp1[0]][tmp1[1]] > 0:
            L[cl[j][0]][cl[j][1]] += 1
        if 0<=tmp2[0]<N and 0<=tmp2[1]<N and L[tmp2[0]][tmp2[1]] > 0:
            L[cl[j][0]][cl[j][1]] += 1
        if 0<=tmp3[0]<N and 0<=tmp3[1]<N and L[tmp3[0]][tmp3[1]] > 0:
            L[cl[j][0]][cl[j][1]] += 1
        if 0<=tmp4[0]<N and 0<=tmp4[1]<N and L[tmp4[0]][tmp4[1]] > 0:
            L[cl[j][0]][cl[j][1]] += 1
    cl2 = list()
    for j in range(N):
        for k in range(N):
            if L[j][k] >=2 and (j,k) not in cl:
                cl2.append((j,k))
                L[j][k] -=2
    cl = cl2
ans = 0
for i in range(N):
    for j in range(N):
        ans += L[i][j]
print(ans)
