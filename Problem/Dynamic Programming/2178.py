from collections import deque

N, M = map(int, input().split())
L = [[0] * M for _ in range(N)]
s = list
for i in range(N):
    A = input()
    for j in range(len(A)):
        L[i][j] = int(A[j])
q = [[0, 0]]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# i-> 행 j->열
while q:
    a, b = q[0][0], q[0][1]
    del q[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < N and 0 <= y < M and L[x][y] == 1:
            q.append([x, y])
            L[x][y] = L[a][b] + 1

print(L[N - 1][M - 1])
