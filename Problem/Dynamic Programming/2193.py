from collections import deque
N = int(input())
dp = [0 for _ in range(N)]
if N==1:
    print(1)
    exit(0)
for i in range(1,N):
    if i==1:
        dp[i] = 1
    elif i==2:
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + dp[i-2] 
print(dp[-1])