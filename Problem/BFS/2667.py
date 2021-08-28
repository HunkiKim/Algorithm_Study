from collections import deque

N = int(input())
V = []
L = [[] for _ in range(N)]
for i in range(N):
    S = input()
    for j in S:
        L[i].append(j)
O = list()
for i in range(N):  # i-> y j -> x
    for j in range(N):
        if L[i][j] == '1':
            O.append((j, i))
Ans = []
cnt = 0
x = [1, 0, -1, 0]
y = [0, 1, 0, -1]


def bfs(n, N):
    dq = deque()
    dq.append(n)
    c = 0
    while dq:
        T = dq.popleft()
        if T in V:
            continue
        V.append(T)
        c += 1
        for i in range(4):
            tx = T[0] + x[i]
            ty = T[1] + y[i]
            if tx >= 0 and ty >= 0 and tx < N and ty < N:
                if L[ty][tx] == '1' and (tx, ty) not in V:
                    dq.append((tx, ty))

    Ans.append(c)


for i in range(N):
    for j in range(N):
        if L[i][j] == '1' and (j, i) not in V:
            bfs((j, i), N)

print(len(Ans))
Ans.sort()
for i in Ans:
    print(i)