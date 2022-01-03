import heapq
from collections import deque
V,E = map(int,input().split())
L = list()
Visit = [0 for _ in range(0,V+1)]
D = {}
for i in range(E):
    A,B,C = map(int,input().split())
    if A not in D:
        D[A] = [(C,B)]
    else:
        D[A].append((C,B))
    if B not in D:
        D[B] = [(C,A)]
    else:
        D[B].append((C,A))

Ans = [10000000 for _ in range(0,V+1)]
ans = 0
L.append((0,1))
cnt = 0
while L:
    # print(L,Visit)
    if cnt==V:
        break
    P = heapq.heappop(L)
    if Visit[P[1]] == 0:
        cnt += 1
        ans += P[0]
        Visit[P[1]] = 1
        for i in D[P[1]]:
            heapq.heappush(L,i)
if V == 1:
    print(Ans[1])
    exit(0)

print(ans)
        
