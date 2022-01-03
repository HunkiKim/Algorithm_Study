import heapq
import sys
from collections import deque
x = [1,-1,0,0]
y = [0,0,1,-1]
cnt = 1
while True:
    N = int(input())
    V = [[10000000 for _ in range(N)] for _ in range(N)]
    if N==0:
        break
    L = list()
    for i in range(N):
        tmp = list(map(int,input().split())).
        L.append(tmp)
    V[0][0] = L[0][0]
    dq = list()
    dq.append((L[0][0],0,0))
    while dq:

        dp = heapq.heappop(dq)
        # print(dp)
        i = dp[2]
        j = dp[1]
        v = dp[0]
        for k in range(4):
            tmpx = x[k] + j
            tmpy = y[k] + i
            if 0<=tmpx<N and 0<=tmpy<N:
                if V[tmpy][tmpx] > v + L[tmpy][tmpx]:
                    V[tmpy][tmpx] = L[tmpy][tmpx] + v
                    heapq.heappush(dq,(L[tmpy][tmpx]+v,tmpx,tmpy))
                    
    print('Problem ' + str(cnt) + ':', V[-1][-1])
    cnt += 1            
    # print(V)        

    # print(L)

