A = int(input())
dp = [0] * (A + 1)
dp[0] = 1
dp[1] = 3
for i in range(2, A + 1):
    dp[i] = dp[i - 1] * 2 + dp[i - 2]
    dp[i] = dp[i] % 9901
print(dp[A])
