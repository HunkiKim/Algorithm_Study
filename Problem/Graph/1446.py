N,d = input().split()
N,d = int(N), int(d)
D = {}
for i in range(N):
    A,B,W = input().split()
    A,B,W = int(A), int(B), int(W)
    if B not in D:
        D[B] = [(A,W)]
    else:
        D[B].append((A,W))

dp = [1000000 for _ in range(d+1)]
dp[0] = 0
for i in range(1,d+1):
    if i not in D:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1] + 1
        for j in D[i]:
            dp[i] = min(dp[j[0]] + j[1],dp[i])
print(dp[-1])