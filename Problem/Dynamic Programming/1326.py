from collections import deque
N = int(input())
L = list(map(int,input().split()))
visit = [-1 for _ in range(N)]
a,b = map(int,input().split())
a-=1
b-=1
dq = deque()
dq.append(a)
visit[a] = 0
ans = 0
while dq:
    p = dq.popleft()
    cnt = 1
    while True:
        pr = p+cnt*L[p]
        pl = p-cnt*L[p]
        if pl<0 and pr>=N:
            break
        if 0<=pl<N and visit[pl]==-1:
            visit[pl] = visit[p] + 1
            dq.append(pl)
        if 0<=pr<N and visit[pr]==-1:
            visit[pr] = visit[p] + 1
            dq.append(pr)
        cnt+=1

print(visit[b])
