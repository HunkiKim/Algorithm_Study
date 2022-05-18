from collections import defaultdict
import math
import heapq
N, E = map(int,input().split())
D = defaultdict(list)
L = list()
L.append(0)
for i in range(N):
    L.append(math.inf)
for i in range(E):
    a,b,w = map(int,input().split())
    D[a].append((w,b))
    D[b].append((w,a))
v1,v2 = map(int,input().split())
D1 = [math.inf for _ in range(N+1)]
D2 = [math.inf for _ in range(N+1)]
D3 = [math.inf for _ in range(N+1)]
hq = list()
heapq.heappush(hq,(0,1))
D1[1] = 0
while hq:
    entity = heapq.heappop(hq)
    for i in D[entity[1]]:
        if D1[i[1]] > D1[entity[1]] + i[0]:
            D1[i[1]] = D1[entity[1]] + i[0]
            heapq.heappush(hq,i)
hq = list()
heapq.heappush(hq,(0,v1))
D2[v1] = 0
while hq:
    entity = heapq.heappop(hq)
    for i in D[entity[1]]:
        if D2[i[1]] > D2[entity[1]] + i[0]:
            D2[i[1]] = D2[entity[1]] + i[0]
            heapq.heappush(hq,i)
hq = list()
heapq.heappush(hq,(0,v2))
D3[v2] = 0
while hq:
    entity = heapq.heappop(hq)
    for i in D[entity[1]]:
        if D3[i[1]] > D3[entity[1]] + i[0]:
            D3[i[1]] = D3[entity[1]] + i[0]
            heapq.heappush(hq,i)
answer = min(D1[v1]+D2[v2]+D3[N], D1[v2]+D3[v1]+D2[N])
if answer == math.inf:
    print(-1)
else:
    print(answer)
