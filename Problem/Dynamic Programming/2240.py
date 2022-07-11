n = int(input())
INF = 2000
bag = [3,5]
dp = [INF] * (5001)
dp[3] = dp[5] = 1

for i in bag:
    for j in range(i, n+1):
        dp[j] = min(dp[j-i]+1, dp[j])
        print(dp)
print(dp[n] if dp[n] < 2000 else -1)
