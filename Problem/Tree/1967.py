N = int(input())
T = {}
for i in range(N - 1):
    A, B, C = map(int, input().split())
    if A not in T:
        T[A] = [(B, C)]
    else:
        T[A].append((B, C))
Ans = {}


def dfs(n, p, cnt):
    print(n)
    if n not in T:
        if p not in Ans:
            Ans[p] = cnt
        return cnt
    if len(T[n]) == 2:
        if T[n][0][1] > T[n][1][1]:
            Ans[p] = dfs(T[n][0][0], n, T[n][0][1]) + T[n][0][1]
            dfs(T[n][1][0], n, T[n][1][1])
        elif T[n][0][1] < T[n][1][1]:
            Ans[p] = dfs(T[n][1][0], n, T[n][1][1]) + T[n][1][1]
            Ans[p] += dfs(T[n][0][0], n, T[n][0][1])
    else:
        Ans[p] = dfs(T[n][0][0], n, T[n][0][1]) + T[n][0][1]
    return Ans[p]


dfs(1, 1, 0)
print(Ans)