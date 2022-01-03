from collections import deque
N,M = map(int,input().split())
D = {}

# def dfs(n,cnt,V):
#     print(n,cnt)
#     if n not in D or n in V:
#         return cnt
#     L = D[n]
#     V.append(n)
#     cnt += 1
#     for i in L:
#         cnt = dfs(i,cnt,V)
#     return cnt

for i in range(M):
    A,B = map(int , input().split())
    if B not in D:
        D[B] = [A]
    else:
        D[B].append(A)

dq = deque()
Ans = list()
ans = 0

for i in range(1,N+1):
    V = [0 for _ in range(N+1)]
    dq.append(i)
    V[i] = 1
    cnt = 1
    while dq:
        p = dq.popleft()
        
        if p not in D:
            continue
        for j in D[p]:
            if V[j]==0:
                dq.append(j)
                V[j] = 1
                cnt += 1
    if ans < cnt:
        Ans = list()
        Ans.append(i)
        ans = cnt
    elif ans == cnt:
        Ans.append(i)
    # print(cnt)
# for i in range(1,N+1):
#     tmp = dfs(i,0,[])
#     print(tmp,i,"tmp")
#     if tmp > ans:
#         Ans = list()
#         Ans.append(i)
#         ans = tmp
#     elif tmp == ans:
#         Ans.append(i)
#         ans = tmp
for i in Ans:
    print(i, end = " ")
    