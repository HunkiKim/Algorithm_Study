from collections import deque

T = int(input())


def dfs(y, x, M, N):
    if L[y][x] == 1:
        dpx = [1, -1, 0, 0]
        dpy = [0, 0, 1, -1]
        L[y][x] = 0
        for i in range(4):
            if 0 <= y + dpy[i] < N and 0 <= x + dpx[i] < M:
                if L[y + dpy[i]][x + dpx[i]] == 1:
                    dfs(y + dpy[i], x + dpx[i], M, N)


for i in range(T):
    dq = deque()
    M, N, K = map(int, input().split())
    V = [[0] * M for _ in range(N)]
    dpx = [1, 0, -1, 0]
    dpy = [0, 1, 0, -1]
    cnt = 0
    L = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        L[y][x] = 1

    for k in range(N):
        for q in range(M):
            if L[k][q] == 1:
                cnt += 1
                dfs(k, q, M, N)
                # while dq:
                #     y1 = dq[0][0]
                #     x1 = dq[0][1]
                #     dq.pop()
                #     if L[y1][x1] == 0:
                #         continue
                #     L[y1][x1] = 0
                #     for j in range(4):
                #         a = y1 + dpy[j]
                #         b = x1 + dpx[j]
                #         if 0 <= a < N and 0 <= b < M:
                #             if L[a][b] == 1:
                #                 dq.append([a, b])

    print(cnt)