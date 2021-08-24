N = int(input())
L = list()
for i in range(N):
    L.append(input())
ans = 0
V = [0] * N
Ans = [0] * N


def dfs(idx, cnt, cc):
    ans = cnt
    if V[idx] == 1:
        return ans
    if cc >= N or idx >= N:
        return ans
    V[idx] = 1
    for i in range(N):
        if i == idx:
            continue
        else:
            if L[idx][i] == 'Y':
                Ans[cc] += dfs(i, ans + 1, cc)
    V.clear()
    dfs(0, 0, cc + 1)
    return ans


dfs(0, 0, 0)
print(Ans)
