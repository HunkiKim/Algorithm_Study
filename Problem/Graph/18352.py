from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline
dq = deque()
visit = list()
D = defaultdict(list)
N,M,K,X = map(int,input().split())
for i in range(M):
    a,b = map(int,input().split())
    D[a].append(b)

dq.append(X)
visit.append(-1)
for i in range(1,N+1):
    visit.append(-1)
visit[X] = 0
ans = list()
while dq:
    p = dq.popleft()
    if visit[p] == K:
        ans.append(p)
    for i in D[p]:
        if visit[i] == -1:
            visit[i] = visit[p] + 1
            dq.append(i)
if len(ans)==0:
    print(-1)
    exit(0)
else:
    ans.sort()
    for i in ans:
        print(i)
    