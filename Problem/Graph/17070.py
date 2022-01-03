from collections import deque
# def dfs(y,x,dy,dx):
#     global N,ans
#     if y==N-1 and x==N-1:
#         ans += 1
#         return

#     for i in c:
#         y1 = y + i[0]
#         x1 = x + i[1]
#         if (dy == 0 and dx == 1 and i[0] == 1 and i[1] == 0) or (dy == 1 and dx == 0 and i[0] == 0 and i[1] == 1):
#             continue
#         if 0<=y1<N and 0<=x1<N and L[y1][x1] != 1:
#             if i[0] == 0 or i[1] == 0:
#                 if L[y1][x1] != 1:
#                     dfs(y,x,i[0],i[1])
#             else:
#                 if L[y1][x1] != 1 and L[y1-1][x1] != 1 and L[y1][x1-1] != 1:
#                     dfs(y,x,i[0],i[1])
N = int(input())
L = list()
V = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    L.append(list(map(int,input().split())))
c = [(0,1), (1,0), (1,1)]
dp = list()
dp.append([[0 for _ in range(N)] for _ in range(N)])
dp.append([[0 for _ in range(N)] for _ in range(N)])
dp.append([[0 for _ in range(N)] for _ in range(N)])
dp[0][0][1] = 1
for i in range(N):
    for j in range(0,N):
        for k in c:
            y1 = k[0] + i
            x1 = k[1] + j
            
            if 0<=y1<N and 0<=x1<N and L[y1][x1]!=1:
                # print(y1,x1,dp)
                if k[0] == 1 and k[1] == 1:    
                    dp[0][y1][x1] += dp[1][y1-1][x1-1] + dp[0][y1][x1-1]
                    dp[1][y1][x1] += dp[0][y1][x1-1] + dp[1][y1-1][x1-1] + dp[2][y1-1][x1]
                    dp[2][y1][x1] += dp[1][y1-1][x1-1] + dp[2][y1-1][x1]
                elif k[0] == 0 and k[1] == 1:
                    dp[0][y1][x1] += dp[1][y1-1][x1-1] + dp[0][y1][x1-1]
                    dp[1][y1][x1] += dp[0][y1][x1-1] + dp[1][y1-1][x1-1] + dp[2][y1-1][x1]
                else:
                    dp[1][y1][x1] += dp[0][y1][x1-1] + dp[1][y1-1][x1-1] + dp[2][y1-1][x1]
                    dp[2][y1][x1] += dp[1][y1-1][x1-1] + dp[2][y1-1][x1]

ans = dp[0][N-1][N-1] + dp[1][N-1][N-1] +dp[2][N-1][N-1] 
print(ans,dp)