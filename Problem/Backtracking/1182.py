N, S = map(int, input().split())
L = list(map(int, input().split()))
C = 0
VV = list()


def dfs(index, ans):
    global C, S, p
    # print(V, ans)
    if index == N:
        return
    ans += L[index]
    if ans == S:
        C += 1

    dfs(index + 1, ans - L[index])  #00000
    dfs(index + 1, ans)


def solution():
    V = [0 for _ in range(N)]
    dfs(0, 0)  # 00000
    print(C)
    # print(C)


solution()