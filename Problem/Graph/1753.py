from collections import deque
import heapq
V,E = map(int,input().split())
start = int(input())
L = []
D = {}
INF = 400000

for i in range(E):
    a,b,w = map(int,input().split())
    if a in D:
        D[a].append((w,b,a))
    else:
        D[a] = [(w,b,a)]

Ans = []
for i in range(V+1):
    if i==start:
        Ans.append(0)
    else:
        Ans.append(INF)
L = [(0,start)]
while L:
    p = heapq.heappop(L)
    
    w,v = p[0], p[1]
    if v in D:
        for i in D[v]:
            if Ans[i[1]] > w + i[0]:
                Ans[i[1]] = w + i[0]
                heapq.heappush(L,(Ans[i[1]],i[1]))

for i in range(1,V+1):
    if INF == Ans[i]:
        print("INF")
    else:
        print(Ans[i])
