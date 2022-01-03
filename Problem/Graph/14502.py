from collections import deque
import copy
L = list()

ans = 0
V = {}


def bfs():
    global zcnt
    global ans
    stack = deque()
    LC = copy.deepcopy(L)
    for i in range(len(L)):
        for j in range(len(L[0])):
            if LC[i][j] == 2:
                stack.append((i, j))

    while stack:
        tmp = stack.popleft()
        y = tmp[0]
        x = tmp[1]
        for k in range(4):
            nx = X[k] + x
            ny = Y[k] + y
            if 0 <= nx < len(L[0]) and 0 <= ny < len(L):
                if LC[ny][nx] == 0:
                    LC[ny][nx] = 2
                    stack.append((ny, nx))
    # print(LC)
    tmp = 0
    for i in LC:
        tmp += i.count(0)
    ans = max(ans, tmp)


def dfs(cnt):
    global zcnt
    global ans
    # print('s')
    if cnt == 3:
        bfs()
        return
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == 0:
                L[i][j] = 1
                dfs(cnt + 1)
                L[i][j] = 0


R, C = map(int, input().split())
for i in range(R):
    L.append(list(map(int, input().split())))
# print(L)
zcnt = 0
for i in L:
    zcnt += i.count(0)
# print(zcnt)
zcnt = zcnt - 3
X = [1, -1, 0, 0]
Y = [0, 0, 1, -1]
dfs(0)
print(ans)
