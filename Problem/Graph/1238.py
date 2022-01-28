from collections import deque
import heapq
def dijk(start):
    global M
    T = [1000000 for _ in range(M+1)]
    T[start] = 0
    # for i,j in D[start]:
    #     T[i] = j
    dq = list()
    dq.append((0,start))
    # print(T)
    while dq:
        w,p = heapq.heappop(dq)
        for i,j in D[p]:
            if j+T[p] < T[i]:
                T[i] = j+T[p]
                heapq.heappush(dq,(T,i))
    LL.append(T)

M,N,X = map(int,input().split())
D = {}
for i in range(1,M+1):
    D[i] = []
for i in range(N):
    a,b,w = map(int,input().split())
    D[a].append((b,w))

dq = deque()
A_X = [0 for _ in range(M+1)]
LL = list()
ans = 0
LL.append([0 for _ in range(M+1)])
for i in range(1,M+1):
    dijk(i)
for i in range(1,M+1):
    if i==X:
        continue
    ans = max(LL[i][X] + LL[X][i],ans)
print(ans)
